#!/usr/bin/env python3
"""
Sistema Agentico de Inteligencia Competitiva — Fase 2
Penetracion de 50 Doctors en el mercado espanol de salud

Arquitectura multi-agente:
  Agent OSINT     → Datos publicos (webs corporativas, informes, regulacion)
  Agent Alt.Data  → Senales debiles (M&A, noticias, planes expansion)
  Agent AMC       → Analisis Awareness / Motivation / Capability (Chen & Miller 2012)
  Agent Sintesis  → Integracion en informe y matrices

Uso:
    python agentic_intelligence_system.py
    python agentic_intelligence_system.py --competidor sanitas
    python agentic_intelligence_system.py --export json
"""

import json
import argparse
from dataclasses import dataclass, asdict, field
from typing import List, Dict, Optional
from datetime import datetime


# ---------------------------------------------------------------------------
# Modelos de datos
# ---------------------------------------------------------------------------

@dataclass
class DataSource:
    """Fuente de datos verificada con evidencia."""
    id: int
    nombre: str
    tipo: str               # OSINT | Alt.Data | Primaria/Publica
    lead_time: str
    framework_link: str     # Awareness | Motivation | Capability | Contexto
    url: str
    evidencia: str
    estado: str = "completado"


@dataclass
class AMCScore:
    """Puntuacion AMC para un competidor (Chen & Miller 2012)."""
    competidor: str
    awareness: int                  # 1-5
    awareness_evidencia: List[str]
    motivation: int                 # 1-5
    motivation_evidencia: List[str]
    capability: int                 # 1-5
    capability_evidencia: List[str]
    p_respuesta: float              # % probabilidad
    timeline_meses_min: int
    timeline_meses_max: int
    tipo_respuesta: List[Dict[str, float]]  # [{tipo: prob}, ...]
    fecha: str = ""

    def __post_init__(self):
        if not self.fecha:
            self.fecha = datetime.now().strftime("%Y-%m-%d")


# ---------------------------------------------------------------------------
# Agent OSINT — Datos publicos
# ---------------------------------------------------------------------------

class OSINTAgent:
    """Recopila datos de fuentes publicas verificables."""

    nombre = "Agent OSINT"

    @staticmethod
    def fuentes_verificadas() -> List[DataSource]:
        return [
            DataSource(1, "Webs corporativas Sanitas/Adeslas/Asisa/HLA",
                       "OSINT", "1-2 dias", "Awareness/Capability",
                       "sanitas.es, segurcaixaadeslas.es, asisa.es, grupohla.com",
                       "Estructuras corporativas, red asistencial, servicios"),
            DataSource(2, "Informes anuales (Sanitas 2024, Mutua 2024-25, ASISA 2024-25)",
                       "Primaria/Publica", "1 mes", "Capability",
                       "informeanual.sanitas.es, grupomutua.es, asisa.es",
                       "Financieros completos verificados"),
            DataSource(3, "BUPA Group Results FY2024 + H1 2025",
                       "Primaria/Publica", "Trimestral", "Capability",
                       "bupa.com/news-and-press",
                       "Revenue ELA 5.427M GBP, estructura Mexico, M&A"),
            DataSource(4, "UNESPA informe diciembre 2025",
                       "Primaria/Publica", "Mensual", "Contexto",
                       "unespa.es",
                       "Primas 13.443M EUR, 13M asegurados"),
            DataSource(6, "DGSFP prioridades supervision 2023-2025",
                       "Publica/Regulatoria", "Anual", "Capability",
                       "dgsfp.mineco.gob.es",
                       "ALOSSEAR, sandbox, sin tope primas"),
            DataSource(8, "Fundacion Espriu / Compartir (ASISA int.)",
                       "OSINT", "2 semanas", "Awareness",
                       "fundacionespriu.coop, compartir.coop",
                       "ASISA presente en Mexico, Nicaragua, Italia, Portugal"),
            DataSource(9, "IBM Case Study — Adeslas",
                       "OSINT", "1-2 dias", "Capability",
                       "ibm.com/case-studies/segurcaixa-adeslas",
                       "Modernizacion API Connect v10"),
        ]


# ---------------------------------------------------------------------------
# Agent Alt.Data — Senales debiles
# ---------------------------------------------------------------------------

class AltDataAgent:
    """Busca indicadores de movimiento estrategico en fuentes alternativas."""

    nombre = "Agent Alt.Data"

    @staticmethod
    def fuentes_verificadas() -> List[DataSource]:
        return [
            DataSource(5, "Prensa financiera (El Economista, El Espanol, OKDiario)",
                       "Primaria", "Semanal", "Motivation",
                       "eleconomista.es, elespanol.com, okdiario.com",
                       "Resultados, MUFACE, expansion, estrategia"),
            DataSource(7, "Noticias 50 Doctors (NITU, Gob QRoo, Diario Financiero)",
                       "Alt.Data", "Tiempo real", "Awareness",
                       "nitu.mx, qroo.gob.mx, diariofinanciero.com",
                       "Planes Espana: Madrid Serrano, BCN, Coruna, Malaga"),
            DataSource(10, "Tracxn + Latin Lawyer (BUPA M&A)",
                       "Alt.Data", "1 semana", "Capability/Motivation",
                       "tracxn.com, latinlawyer.com",
                       "Historial adquisiciones BUPA 2020-2025"),
            DataSource(11, "Ministerio Turismo + Redaccion Medica",
                       "Publica", "1 mes", "Contexto",
                       "turismo.gob.es, redaccionmedica.com",
                       "200K turistas salud/ano, 1.000M EUR, +28% 2024"),
            DataSource(12, "Halcones y Palomas (Mutua Colombia)",
                       "Alt.Data", "Tiempo real", "Motivation",
                       "halconesypalomas.com",
                       "Mutua compra 100% Seguros del Estado Colombia"),
        ]


# ---------------------------------------------------------------------------
# Agent AMC — Analisis competitivo (Chen & Miller 2012)
# ---------------------------------------------------------------------------

class AMCAgent:
    """Genera puntuaciones AMC ponderadas con evidencia."""

    nombre = "Agent AMC"

    # Pesos para calculo P(respuesta): A x wA + M x wM + C x wC
    W_AWARENESS = 0.30
    W_MOTIVATION = 0.40
    W_CAPABILITY = 0.30

    @classmethod
    def _p_respuesta_bruta(cls, a: int, m: int, c: int) -> float:
        """Probabilidad bruta = media ponderada normalizada a %."""
        score = a * cls.W_AWARENESS + m * cls.W_MOTIVATION + c * cls.W_CAPABILITY
        return (score / 5.0) * 100

    @staticmethod
    def analizar_sanitas() -> AMCScore:
        return AMCScore(
            competidor="Sanitas (BUPA)",
            awareness=5,
            awareness_evidencia=[
                "BUPA opera en Mexico: Vitamedica (7.500+ proveedores, 2020), Hospital Bite Medica (CDMX, 2022)",
                "BUPA en 10+ paises Latam (Chile, Brasil, Colombia, Peru, etc.)",
                "Sanitas lidera BUPA ELA desde Madrid — gestiona operaciones Mexico directamente",
                "Planes de 50 Doctors para Calle Serrano (Madrid) son informacion publica",
            ],
            motivation=4,
            motivation_evidencia=[
                "Ingresos +12% (2025: 3.228M EUR), record 533K nuevas polizas",
                "Hospital Blua Valdebebas (jun 2025): diferenciacion digital",
                "BUPA ELA = 36% beneficio grupo → presion por defender Espana",
                "M&A activo 2025: Magnus (Polonia), Dental Star (Espana)",
                "Motivacion dual: defensiva (proteger) + ofensiva (50 Doctors como partner)",
            ],
            capability=5,
            capability_evidencia=[
                "BUPA: ingresos ELA 5.427M GBP, ~87.000 empleados globales",
                "Historial M&A multinacional probado (8 paises ELA)",
                "Hospital Blua con IA (SaniTask, SaniResult), 928K consultas digitales",
                "11.352 empleados Espana (+6%), estructura legal internacional",
            ],
            p_respuesta=87.0,  # 92% bruto - 5% ajuste inercia
            timeline_meses_min=3,
            timeline_meses_max=6,
            tipo_respuesta=[
                {"alianza_estrategica": 0.40},
                {"contraofensiva_competitiva": 0.30},
                {"observacion_activa": 0.20},
                {"adquisicion_inversion": 0.10},
            ],
        )

    @staticmethod
    def analizar_adeslas() -> AMCScore:
        return AMCScore(
            competidor="Adeslas (Mutua/CaixaBank)",
            awareness=3,
            awareness_evidencia=[
                "Latam: Chile (BCI Seguros 60%) + Colombia (Seguros del Estado 45%→100%)",
                "NO opera en Mexico — sin contacto directo con 50 Doctors",
                "Pero planes de 50 Doctors para Madrid son publicos",
                "Monitorea sector hospitalario espanol por su red contratada",
            ],
            motivation=3,
            motivation_evidencia=[
                "Crecimiento fuerte: Adeslas 5.950M EUR (+12,5%), beneficio +31%",
                "Record 19M+ asegurados, 5,4M polizas",
                "No posee hospitales → 50 Doctors podria ser PROVEEDOR, no competidor",
                "MUFACE: nuevo contrato 2025-2027 mejora condiciones",
                "Modelo complementario reduce urgencia de reaccion",
            ],
            capability=5,
            capability_evidencia=[
                "Grupo mas grande: 9.757M EUR ingresos (2025)",
                "CaixaBank = canal distribucion masivo",
                "M&A internacional exitoso: Chile, Colombia",
                "IBM partnership para modernizacion digital",
            ],
            p_respuesta=60.0,  # 72% bruto - 12% modelo complementario
            timeline_meses_min=6,
            timeline_meses_max=12,
            tipo_respuesta=[
                {"incorporar_red_contratada": 0.45},
                {"observacion_activa": 0.30},
                {"producto_premium_propio": 0.15},
                {"ignorar": 0.10},
            ],
        )

    @staticmethod
    def analizar_asisa() -> AMCScore:
        return AMCScore(
            competidor="Asisa (HLA)",
            awareness=3,
            awareness_evidencia=[
                "ASISA tiene presencia en Mexico (confirmado Fundacion Espriu)",
                "Tambien Nicaragua, Portugal, Italia, Suiza, Oriente Medio",
                "ASISA Dental: 50+ clinicas internacionales",
                "Internacionalizacion es pilar estrategico declarado",
                "HLA Internacional Barcelona (2023, 25M EUR)",
            ],
            motivation=4,
            motivation_evidencia=[
                "2025: mejor ejercicio historia (primas 1.890M EUR, +21,1%)",
                "UNICO de los 3 que posee/opera hospitales → competidor DIRECTO",
                "HLA opera en Madrid, Barcelona, Malaga = mismas ciudades que 50 Doctors",
                "155M EUR invertidos en modernizacion HLA desde 2020",
                "Amenaza directa al core business (gestion hospitalaria)",
            ],
            capability=3,
            capability_evidencia=[
                "Facturacion >2.616M EUR (2025) — significativa pero menor",
                "Red HLA solida (18 hospitales, 38 centros)",
                "Modelo cooperativo: decisiones mas lentas",
                "Sin respaldo de cotizada o grupo financiero potente",
                "Experiencia hospital internacional limitada (solo Barcelona)",
            ],
            p_respuesta=55.0,  # 68% bruto - 13% limitaciones financieras
            timeline_meses_min=6,
            timeline_meses_max=9,
            tipo_respuesta=[
                {"alianza_defensiva": 0.35},
                {"refuerzo_competitivo": 0.30},
                {"integracion_red": 0.25},
                {"observar_esperar": 0.10},
            ],
        )


# ---------------------------------------------------------------------------
# Agent Sintesis — Genera informe integrado
# ---------------------------------------------------------------------------

class SynthesisAgent:
    """Integra outputs de todos los agentes en informe cohesionado."""

    nombre = "Agent Sintesis"

    @staticmethod
    def generar_resumen(
        fuentes: List[DataSource],
        scores: List[AMCScore],
    ) -> str:
        lineas = []
        lineas.append("=" * 70)
        lineas.append("  SISTEMA AGENTICO — INTELIGENCIA COMPETITIVA FASE 2")
        lineas.append("  50 Doctors: penetracion mercado espanol")
        lineas.append("=" * 70)

        lineas.append(f"\n  Fuentes verificadas: {len(fuentes)}")
        lineas.append(f"  Competidores analizados: {len(scores)}")
        lineas.append(f"  Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

        lineas.append("\n" + "-" * 70)
        lineas.append("  MATRIZ AMC (Chen & Miller 2012)")
        lineas.append("-" * 70)
        lineas.append(f"  {'Competidor':<28} {'A':>3} {'M':>3} {'C':>3}  {'P(Resp)':>8}  {'Timeline':>12}")
        lineas.append("  " + "-" * 64)
        for s in scores:
            tl = f"{s.timeline_meses_min}-{s.timeline_meses_max} meses"
            lineas.append(
                f"  {s.competidor:<28} {s.awareness:>3} {s.motivation:>3} {s.capability:>3}"
                f"  {s.p_respuesta:>7.1f}%  {tl:>12}"
            )

        lineas.append("\n" + "-" * 70)
        lineas.append("  FUENTES DE DATOS (12 verificadas)")
        lineas.append("-" * 70)
        for f in fuentes:
            lineas.append(f"  [{f.id:>2}] {f.nombre[:50]:<50} {f.tipo:<20} {f.framework_link}")

        lineas.append("\n" + "-" * 70)
        lineas.append("  CONCLUSIONES")
        lineas.append("-" * 70)
        ranking = sorted(scores, key=lambda s: s.p_respuesta, reverse=True)
        for i, s in enumerate(ranking, 1):
            resp_principal = max(s.tipo_respuesta, key=lambda d: list(d.values())[0])
            tipo = list(resp_principal.keys())[0].replace("_", " ").title()
            prob = list(resp_principal.values())[0] * 100
            lineas.append(
                f"  {i}. {s.competidor}: P={s.p_respuesta:.0f}% "
                f"| Respuesta mas probable: {tipo} ({prob:.0f}%)"
            )

        lineas.append("\n" + "=" * 70)
        return "\n".join(lineas)


# ---------------------------------------------------------------------------
# Orquestador principal
# ---------------------------------------------------------------------------

class IntelligenceSystem:
    """Orquesta los 4 agentes y genera outputs."""

    def __init__(self):
        self.osint = OSINTAgent()
        self.altdata = AltDataAgent()
        self.amc = AMCAgent()
        self.synthesis = SynthesisAgent()

    def ejecutar(self, export_json: bool = False, competidor: Optional[str] = None):
        # 1. Recopilar fuentes
        fuentes = self.osint.fuentes_verificadas() + self.altdata.fuentes_verificadas()
        print(f"[Agent OSINT]    {len(self.osint.fuentes_verificadas())} fuentes publicas")
        print(f"[Agent Alt.Data] {len(self.altdata.fuentes_verificadas())} fuentes alternativas")
        print(f"[Total]          {len(fuentes)} fuentes verificadas\n")

        # 2. Analisis AMC
        scores = [
            self.amc.analizar_sanitas(),
            self.amc.analizar_adeslas(),
            self.amc.analizar_asisa(),
        ]

        if competidor:
            scores = [s for s in scores if competidor.lower() in s.competidor.lower()]

        print(f"[Agent AMC]      {len(scores)} competidores analizados\n")

        # 3. Sintesis
        resumen = self.synthesis.generar_resumen(fuentes, scores)
        print(resumen)

        # 4. Export
        if export_json:
            data = {
                "fecha": datetime.now().isoformat(),
                "fuentes": [asdict(f) for f in fuentes],
                "amc_scores": [asdict(s) for s in scores],
            }
            with open("resultados_amc.json", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"\n  Exportado: resultados_amc.json")

        return fuentes, scores


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sistema Agentico — Inteligencia Competitiva Fase 2")
    parser.add_argument("--competidor", type=str, help="Filtrar por competidor (sanitas/adeslas/asisa)")
    parser.add_argument("--export", type=str, choices=["json"], help="Exportar resultados")
    args = parser.parse_args()

    sistema = IntelligenceSystem()
    sistema.ejecutar(
        export_json=(args.export == "json") if args.export else False,
        competidor=args.competidor,
    )
