#!/usr/bin/env python3
"""
Sistema Agentico Early Warning + Strategic Recommendation -- Fase 5
50 Doctors Mexico -- Expansion al mercado espanol de salud

Arquitectura multi-agente:
  Agent KIT      -> Define los 3 Key Intelligence Topics (Gilad, TN03)
  Agent EWS      -> Dashboard 9 KIIs con umbrales y logica de alerta
  Agent Rec      -> Recomendacion estrategica Go/No-Go/Conditional Go
  Agent Sintesis -> Informe ejecutivo integrado

Uso:
    python agentic_ews_system.py
    python agentic_ews_system.py --export json
    python agentic_ews_system.py --recommendation-only
"""

import json
import argparse
from dataclasses import dataclass, asdict
from typing import List, Optional, Tuple
from datetime import datetime
from enum import Enum


class AlertLevel(Enum):
    GREEN = "VERDE"
    YELLOW = "AMARILLO"
    RED = "ROJO"


class Decision(Enum):
    GO = "GO"
    NO_GO = "NO-GO"
    CONDITIONAL_GO = "CONDITIONAL GO"


@dataclass
class KIT:
    id: int
    nombre: str
    pregunta_central: str
    relevancia: str
    owner: str
    fase_origen: str


@dataclass
class KII:
    id: int
    kit_id: int
    indicador: str
    fuente: str
    frecuencia: str
    umbral_alerta: str
    owner: str
    valor_actual: Optional[str] = None
    nivel_alerta: AlertLevel = AlertLevel.GREEN
    notas: str = ""


@dataclass
class EvidencePoint:
    id: int
    fase_origen: str
    hallazgo: str
    implicacion: str
    peso: str


@dataclass
class StrategicAction:
    tipo: str
    accion: str
    responsable: str
    plazo: str
    kpi: str


@dataclass
class StrategicRecommendation:
    decision: Decision
    confidence_pct: float
    razonamiento: str
    evidencias: List[EvidencePoint]
    condiciones_go: List[StrategicAction]
    hedging_actions: List[StrategicAction]
    shaping_actions: List[StrategicAction]
    fecha: str = ""

    def __post_init__(self):
        if not self.fecha:
            self.fecha = datetime.now().strftime("%Y-%m-%d")


# ---------------------------------------------------------------------------
# Agent KIT -- Key Intelligence Topics (Gilad, TN03)
# ---------------------------------------------------------------------------

class KITAgent:
    nombre = "Agent KIT"

    @staticmethod
    def definir_kits() -> List[KIT]:
        return [
            KIT(1,
                "Receptividad de aseguradoras espanolas a alianzas internacionales",
                "Esta Sanitas/BUPA activamente dispuesta a co-invertir en un JV "
                "hospitalario con 50 Doctors en los proximos 6-12 meses?",
                "Supuesto critico ABP #2 (P_fallo=40%): si Sanitas rechaza el JV, "
                "E[NPV] cae de +14.2M a -8M EUR. Mayor determinante de la decision final.",
                "Persona 2", "Fases 2 y 3"),
            KIT(2,
                "Cambios regulatorios en el sector sanitario privado espanol",
                "Introducira la DGS o el Ministerio de Sanidad restricciones a la "
                "inversion extranjera en hospitales privados en 2026-2027?",
                "Supuesto critico ABP #1 (P_fallo=35%): regulacion adversa activa "
                "Escenario C/D (P=50% combinado). En Esc. D la alianza pierde -8M EUR.",
                "Persona 5", "Fases 3 y 4"),
            KIT(3,
                "Movimientos competitivos de Sanitas/Adeslas hacia Mexico/LATAM",
                "Esta BUPA acelerando su expansion hospitalaria en Mexico o LATAM "
                "de forma que reduzca su interes en 50 Doctors como socio?",
                "Supuesto critico ABP #4 (P_fallo=25%): si BUPA prefiere expansion "
                "propia, 50D pierde 25M EUR de valor diferencial (Exchange Value F4).",
                "Persona 2", "Fases 2 y 4"),
        ]


# ---------------------------------------------------------------------------
# Agent EWS -- Early Warning System Dashboard (Gilad, TN03)
# ---------------------------------------------------------------------------

class EWSAgent:
    nombre = "Agent EWS"
    UMBRAL_REVISION_ESTRATEGICA = 2  # KIIs en ROJO que disparan revision total

    @staticmethod
    def definir_kiis() -> List[KII]:
        return [
            # KIT 1 - Receptividad aseguradoras
            KII(1, 1,
                "Job postings 'international partnerships' o 'hospital expansion LATAM' "
                "en LinkedIn Sanitas/BUPA",
                "LinkedIn Jobs + Sales Navigator", "Mensual",
                "ROJO: >3 postings/30d | AMARILLO: 1-3 postings", "Persona 2",
                "Sin datos (inicio monitoreo)", AlertLevel.GREEN,
                "Senal temprana de intent organizacional antes de anuncio publico"),
            KII(2, 1,
                "Menciones prensa financiera 'alianza hospital mexicano' o '50 Doctors Espana'",
                "Google Alerts + Factiva (El Economista, Expansion)", "Diaria",
                "ROJO: >2 menciones/semana | AMARILLO: 1 mencion/semana", "Persona 5",
                "Sin datos (inicio monitoreo)", AlertLevel.GREEN,
                "Priorizar fuentes de calidad financiera sobre prensa generalista"),
            KII(3, 1,
                "NPS / satisfaccion clientes Sanitas y Adeslas (Trustpilot, Google Reviews)",
                "Trustpilot / Redaccion Medica encuestas sectoriales", "Trimestral",
                "ROJO: Caida >5 puntos NPS | AMARILLO: Caida 2-5 puntos", "Persona 1",
                "Sin datos (inicio monitoreo)", AlertLevel.GREEN,
                "Caida de satisfaccion = ventana de oportunidad para modelo 50D premium"),
            # KIT 2 - Regulacion
            KII(4, 2,
                "Nuevas resoluciones DGS sobre inversion extranjera en hospitales privados",
                "BOE (boe.es) + DGSFP (dgsfp.mineco.gob.es)", "Semanal",
                "ROJO: Cualquier resolucion restrictiva | AMARILLO: Consulta publica abierta",
                "Persona 5", "Sin restricciones activas (estado 2026-04)", AlertLevel.GREEN,
                "BOE keywords: inversion extranjera, hospital privado, autorizacion sanitaria"),
            KII(5, 2,
                "Cambios en cobertura minima seguros salud o tarifas concertadas (UNESPA/CCAA)",
                "BOE / UNESPA / CCAA Madrid-Cataluna-Andalucia", "Trimestral",
                "ROJO: Cambio que afecte tarifas JV >10% | AMARILLO: Consulta sobre tarifas",
                "Persona 5", "Legislacion estable (MUFACE renovado 2025-2027)", AlertLevel.GREEN,
                "MUFACE renovado elimina riesgo regulatorio a corto plazo (TN04)"),
            KII(6, 2,
                "Declaraciones publicas Ministro Sanidad o Consejeros CCAA sobre hospitales extranjeros",
                "MSCBS ruedas de prensa + Twitter/X oficial", "Mensual",
                "ROJO: Declaracion hostil directa | AMARILLO: Mencion negativa en contexto politico",
                "Persona 3", "Sin declaraciones relevantes (2026-04)", AlertLevel.GREEN,
                "Anticipa regulacion futura antes de publicacion en BOE"),
            # KIT 3 - Movimientos competitivos LATAM
            KII(7, 3,
                "Anuncios apertura o adquisicion hospitales por Sanitas/BUPA en Mexico o LATAM",
                "CNMC + Prensa financiera + BUPA Group Press Releases", "Mensual",
                "ROJO: Nuevo hospital BUPA en MX (anuncio formal) | AMARILLO: Exploracion publica",
                "Persona 2", "BUPA opera Vitamedica + Hospital Bite Medica CDMX (estables)",
                AlertLevel.GREEN,
                "Si BUPA expande sola en MX puede reducir interes en JV con 50D"),
            KII(8, 3,
                "Movimientos M&A de Adeslas o ASISA en Mexico/LATAM (adquisiciones, JVs)",
                "CNMC + Bloomberg + Latin Lawyer + Tracxn", "Mensual",
                "ROJO: JV con rival directo de 50D en MX | AMARILLO: Due diligence rumoreada",
                "Persona 2", "Adeslas: Colombia (Seguros del Estado 100%). Sin movimientos MX.",
                AlertLevel.GREEN, "Adeslas sin presencia directa en Mexico -- ventana abierta"),
            KII(9, 3,
                "Resultados financieros BUPA ELA H1 2026 (revenue, guidance expansion)",
                "BUPA Group Half-Year Results (bupa.com/news-and-press)", "Semestral",
                "ROJO: Guidance expansion organica Espana >100M EUR sin socio | AMARILLO: Menciones MX",
                "Persona 2", "FY2024: ELA 5.427M GBP (+12%) -- expansion activa", AlertLevel.GREEN,
                "H1 2026 publicacion esperada agosto 2026; monitorizar call de resultados"),
        ]

    @classmethod
    def evaluar_alertas(cls, kiis: List[KII]) -> Tuple[int, int, int]:
        verde = sum(1 for k in kiis if k.nivel_alerta == AlertLevel.GREEN)
        amarillo = sum(1 for k in kiis if k.nivel_alerta == AlertLevel.YELLOW)
        rojo = sum(1 for k in kiis if k.nivel_alerta == AlertLevel.RED)
        return verde, amarillo, rojo

    @classmethod
    def decision_revision_estrategica(cls, rojo: int) -> bool:
        return rojo >= cls.UMBRAL_REVISION_ESTRATEGICA


# ---------------------------------------------------------------------------
# Agent Rec -- Strategic Recommendation
# ---------------------------------------------------------------------------

class RecommendationAgent:
    nombre = "Agent Rec"

    @staticmethod
    def generar_evidencias() -> List[EvidencePoint]:
        return [
            EvidencePoint(1, "Fase 4 -- ECOMO / Decision Tree",
                "Alianza Sanitas/BUPA: unica opcion con E[NPV] positivo y robusto: "
                "+14.2M EUR (vs. Entrada Directa -3.5M EUR; No Entrada 0 EUR). "
                "Mantiene E[NPV] positivo incluso si P(D) sube al 50% (+3.2M EUR).",
                "Inaccion tiene coste de oportunidad real de 14.2M EUR. "
                "El riesgo de accion supera al riesgo de inaccion.",
                "ALTO -- metrica de decision central"),
            EvidencePoint(2, "Fase 2 -- AMC (Chen & Miller 2012)",
                "Sanitas/BUPA: AMC=5/4/5, P(respuesta)=87%, timeline 3-6 meses. "
                "BUPA ya opera en Mexico (Vitamedica, Hospital Bite Medica CDMX). "
                "Tipo de respuesta mas probable: alianza estrategica (40%).",
                "Ventana de negociacion estrecha: si 50D no actua en 6 meses, "
                "BUPA puede priorizar expansion propia (Hospital Blua Valdebebas, jun 2025).",
                "ALTO -- define urgencia de la accion"),
            EvidencePoint(3, "Fase 4 -- Exchange Value Framework",
                "50D captura 96M EUR del Exchange Value total (160M EUR del JV). "
                "Si BUPA financia al WACC 8%, E[NPV] escala de 14.2M a 22.8M EUR (+60%). "
                "Modelo medico-socio genera 25M EUR diferencial que Sanitas no puede replicar sola.",
                "Poder negociador de 50D es real y cuantificable. "
                "Equity minimo a negociar: 55%.",
                "ALTO -- justifica condiciones contractuales del GO"),
        ]

    @staticmethod
    def generar_condiciones_go() -> List[StrategicAction]:
        return [
            StrategicAction("CONDICION GO",
                "Sanitas compromete contractualmente derivacion minima del 20% de capacidad "
                "hospitalaria (garantia 65%+ ocupacion Ano 3 -- supuesto critico ABP #3, P_fallo=45%)",
                "CEO 50D + Equipo Legal", "0-3 meses antes de CapEx",
                "Clausula de volumen garantizado en termsheet del JV"),
            StrategicAction("CONDICION GO",
                "BUPA Group financia su 40% como deuda corporativa (rating A), "
                "reduciendo WACC efectivo de 50D de 12% a 8-10%",
                "CFO 50D + BUPA Group Treasury", "3-6 meses (cierre JV)",
                "Termsheet de financiacion con WACC efectivo <10%"),
            StrategicAction("CONDICION GO",
                "Pre-acuerdo con autoridad sanitaria CCAA Madrid ANTES de iniciar obras, "
                "via relaciones institucionales Sanitas con Comunidad de Madrid",
                "Sanitas (Rel. Institucionales)", "3-6 meses antes de CapEx",
                "Carta de no-oposicion o pre-autorizacion sanitaria CCAA Madrid"),
            StrategicAction("CONDICION GO",
                "Clausula de exit: si Escenario D se materializa, BUPA compra el 60% "
                "de 50D al valor book -- limita perdida maxima 50D a 8M EUR",
                "Legal 50D + M&A Advisor", "En JV Agreement (6 meses)",
                "Clausula put firmada en JV Agreement"),
        ]

    @staticmethod
    def generar_hedging_actions() -> List[StrategicAction]:
        return [
            StrategicAction("HEDGING",
                "Iniciar conversaciones paralelas con Adeslas como opcion secundaria "
                "(E[NPV]=+4.6M EUR): posicionarse como proveedor de su red sin comprometer equity",
                "CEO 50D", "0-6 meses (simultaneo a Sanitas)",
                "Carta de interes Adeslas como red proveedora (no vinculante)"),
            StrategicAction("HEDGING",
                "Presupuestar 2-3M EUR en due diligence regulatoria y legal ANTES de comprometer "
                "CapEx: contratar asesor M&A espanol (Rothschild, KPMG Deal Advisory)",
                "CFO 50D", "Primeros 3 meses",
                "Informe DD entregado antes del termsheet"),
            StrategicAction("HEDGING",
                "Estructurar JV con piloto de 1 hospital (H1 Madrid) antes de comprometer "
                "los 4: limita exposicion maxima a 17M EUR en Ano 0",
                "Board 50D", "Decision en JV Agreement (6 meses)",
                "Clausula expansion escalonada: H2 sujeta a 60% ocupacion H1 en Ano 2"),
        ]

    @staticmethod
    def generar_shaping_actions() -> List[StrategicAction]:
        return [
            StrategicAction("SHAPING",
                "CEO 50D propone alianza formal a CEO Sanitas/BUPA ANTES de cualquier anuncio "
                "publico en Espana: aprovechar ventana de receptividad AMC (3-6 meses)",
                "CEO 50D", "Inmediato (primeros 30 dias)",
                "Reunion C-suite Sanitas/BUPA celebrada y minutes documentados"),
            StrategicAction("SHAPING",
                "Activar red turismo medico Mexico-Espana: publicar casos de exito pacientes "
                "BUPA atendidos en 50D MX para demostrar pipeline 12M EUR/ano diferencial",
                "CMO 50D + BUPA International Relations", "3-6 meses (previo termsheet)",
                "Informe de flujo de pacientes BUPA-MX a 50D (ultimos 12 meses)"),
            StrategicAction("SHAPING",
                "Participar en Foro Nacional de Sanidad Privada (FNSP) y congreso UNESPA 2026 "
                "como ponente: posicionar 50D como referente del modelo medico-socio",
                "CEO 50D + Dir. Relaciones Institucionales", "6-12 meses",
                "Invitacion a ponencia aceptada + 3+ reuniones bilaterales post-evento"),
        ]

    @classmethod
    def generar_recomendacion(cls) -> StrategicRecommendation:
        return StrategicRecommendation(
            decision=Decision.CONDITIONAL_GO,
            confidence_pct=72.0,
            razonamiento=(
                "E[NPV] Alianza Sanitas +14.2M EUR supera con claridad todas las alternativas "
                "bajo los 4 escenarios de Fase 3. CONDITIONAL GO (no GO incondicional) porque "
                "los supuestos criticos de ocupacion Ano 3 (P_fallo=45%) y riesgo regulatorio "
                "(P_fallo=35%) solo son mitigables con clausulas contractuales especificas. "
                "Confidence 72%: certeza alta sobre superioridad de la alianza (E[NPV] robusto "
                "incluso si P(D) sube al 50%) + incertidumbre moderada sobre materializacion "
                "exacta de supuestos operativos (ocupacion, regulacion CCAA, WACC final BUPA)."
            ),
            evidencias=cls.generar_evidencias(),
            condiciones_go=cls.generar_condiciones_go(),
            hedging_actions=cls.generar_hedging_actions(),
            shaping_actions=cls.generar_shaping_actions(),
        )


# ---------------------------------------------------------------------------
# Agent Sintesis -- Informe ejecutivo integrado
# ---------------------------------------------------------------------------

class SynthesisAgent:
    nombre = "Agent Sintesis"

    @staticmethod
    def generar_informe(kits, kiis, rec, alertas, revision_requerida):
        verde, amarillo, rojo = alertas
        L = []
        L.append("=" * 72)
        L.append("  SISTEMA AGENTICO -- EARLY WARNING SYSTEM + RECOMENDACION ESTRATEGICA")
        L.append("  50 Doctors Mexico | Expansion mercado espanol de salud | Fase 5")
        L.append("=" * 72)
        L.append(f"\n  Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        L.append(f"  KITs: {len(kits)} | KIIs: {len(kiis)} | Alertas: {verde}V {amarillo}A {rojo}R")
        if revision_requerida:
            L.append("  *** REVISION ESTRATEGICA INMEDIATA REQUERIDA ***")

        L.append("\n" + "-" * 72)
        L.append("  KEY INTELLIGENCE TOPICS (3 KITs -- Gilad TN03)")
        L.append("-" * 72)
        for kit in kits:
            L.append(f"\n  KIT {kit.id}: {kit.nombre}")
            L.append(f"  Pregunta: {kit.pregunta_central}")
            L.append(f"  Relevancia: {kit.relevancia}")
            L.append(f"  Owner: {kit.owner} | Origen: {kit.fase_origen}")

        L.append("\n" + "-" * 72)
        L.append("  MONITORING DASHBOARD (9 KIIs)")
        L.append("-" * 72)
        L.append(f"  {'#':>2}  {'KIT':>3}  {'Indicador':<38}  {'Frecuencia':<11}  {'Estado':>8}  Owner")
        L.append("  " + "-" * 72)
        for kii in kiis:
            ind = kii.indicador[:38]
            L.append(f"  {kii.id:>2}  {kii.kit_id:>3}  {ind:<38}  "
                     f"{kii.frecuencia:<11}  {kii.nivel_alerta.value:>8}  {kii.owner}")

        L.append("\n  Protocolo de escalado:")
        L.append("  1 KII ROJO    -> revision KIT afectado en 72h")
        L.append("  2+ KIIs ROJO  -> comite de decision convocado en 48h")
        L.append("  3+ KIIs ROJO  -> suspension de compromisos de CapEx")

        L.append("\n" + "-" * 72)
        L.append("  RECOMENDACION ESTRATEGICA (Fase 7)")
        L.append("-" * 72)
        L.append(f"\n  VEREDICTO: {rec.decision.value}  |  Confidence: {rec.confidence_pct:.0f}%")
        L.append(f"\n  {rec.razonamiento}")

        L.append("\n  TOP 3 EVIDENCIAS:")
        for ev in rec.evidencias:
            L.append(f"\n  [{ev.id}] {ev.fase_origen} | Peso: {ev.peso}")
            L.append(f"      Hallazgo: {ev.hallazgo[:90]}")
            L.append(f"      Implicacion: {ev.implicacion[:90]}")

        L.append("\n  CONDICIONES PARA EL GO:")
        for i, c in enumerate(rec.condiciones_go, 1):
            L.append(f"  {i}. {c.accion[:78]}")
            L.append(f"     Responsable: {c.responsable} | Plazo: {c.plazo}")

        L.append("\n  HEDGING ACTIONS (mitigacion de riesgo):")
        for i, h in enumerate(rec.hedging_actions, 1):
            L.append(f"  {i}. {h.accion[:78]}")
            L.append(f"     Plazo: {h.plazo}")

        L.append("\n  SHAPING ACTIONS (influir en el entorno):")
        for i, s in enumerate(rec.shaping_actions, 1):
            L.append(f"  {i}. {s.accion[:78]}")
            L.append(f"     Plazo: {s.plazo} | KPI: {s.kpi[:55]}")

        L.append("\n" + "=" * 72)
        L.append("  FIN DEL INFORME -- Sistema Agentico Fase 5")
        L.append("=" * 72)
        return "\n".join(L)


# ---------------------------------------------------------------------------
# Orquestador principal
# ---------------------------------------------------------------------------

class EarlyWarningSystem:
    def __init__(self):
        self.kit_agent = KITAgent()
        self.ews_agent = EWSAgent()
        self.rec_agent = RecommendationAgent()
        self.synthesis = SynthesisAgent()

    def ejecutar(self, export_json=False, check_alerts=False, recommendation_only=False):
        print("[Agent KIT]      Definiendo Key Intelligence Topics...")
        kits = self.kit_agent.definir_kits()
        print(f"                 {len(kits)} KITs definidos")

        print("[Agent EWS]      Construyendo dashboard de monitoreo...")
        kiis = self.ews_agent.definir_kiis()
        alertas = self.ews_agent.evaluar_alertas(kiis)
        verde, amarillo, rojo = alertas
        revision = self.ews_agent.decision_revision_estrategica(rojo)
        print(f"                 {len(kiis)} KIIs | {verde} VERDE | {amarillo} AMARILLO | {rojo} ROJO")

        print("[Agent Rec]      Generando recomendacion estrategica...")
        rec = self.rec_agent.generar_recomendacion()
        print(f"                 Decision: {rec.decision.value} | Confidence: {rec.confidence_pct:.0f}%")

        print("[Agent Sintesis] Integrando informe ejecutivo...\n")

        if recommendation_only:
            print(f"VEREDICTO: {rec.decision.value}  |  Confidence: {rec.confidence_pct:.0f}%")
            for ev in rec.evidencias:
                print(f"  [{ev.id}] {ev.fase_origen}: {ev.hallazgo[:100]}")
            return

        informe = self.synthesis.generar_informe(kits, kiis, rec, alertas, revision)
        print(informe)

        if export_json:
            data = {
                "fecha": datetime.now().isoformat(),
                "kits": [asdict(k) for k in kits],
                "kiis": [{**asdict(k), "nivel_alerta": k.nivel_alerta.value} for k in kiis],
                "alertas": {"verde": verde, "amarillo": amarillo, "rojo": rojo},
                "revision_requerida": revision,
                "recomendacion": {**asdict(rec), "decision": rec.decision.value},
            }
            with open("resultados_ews_fase5.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print("\n  Exportado: resultados_ews_fase5.json")

        return kits, kiis, rec


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Sistema Agentico EWS + Recomendacion Estrategica -- Fase 5"
    )
    parser.add_argument("--check-alerts", action="store_true")
    parser.add_argument("--export", type=str, choices=["json"])
    parser.add_argument("--recommendation-only", action="store_true")
    args = parser.parse_args()

    sistema = EarlyWarningSystem()
    sistema.ejecutar(
        export_json=(args.export == "json") if args.export else False,
        check_alerts=args.check_alerts,
        recommendation_only=args.recommendation_only,
    )
