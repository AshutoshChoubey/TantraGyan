#!/usr/bin/env python3
"""
Master Execution Pipeline for Tantra Gyan Book Publishing Agents.
Usage:
    python3 agents/run_book_agents.py --all
    python3 agents/run_book_agents.py --plan
    python3 agents/run_book_agents.py --audit
    python3 agents/run_book_agents.py --qa
"""

import sys
import argparse
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from agents.config import BookConfig
from agents.book_orchestrator import BookOrchestratorAgent
from agents.formula_simplifier import FormulaSimplifierAgent
from agents.layman_storyteller import LaymanStorytellerAgent
from agents.chart_diagram_generator import ChartDiagramGeneratorAgent
from agents.visual_authenticity_auditor import VisualAuthenticityAuditorAgent
from agents.chrome_qa_monitor import ChromeQAMonitorAgent
from agents.canva_asset_agent import CanvaAssetAgent
from agents.video_concept_agent import VideoConceptAgent


def main():
    parser = argparse.ArgumentParser(description="Tantra Gyan Book Publishing Multi-Agent Engine")
    parser.add_argument("--all", action="store_true", help="Run complete agent pipeline")
    parser.add_argument("--plan", action="store_true", help="Print orchestrator execution plan")
    parser.add_argument("--audit", action="store_true", help="Run visual authenticity audit")
    parser.add_argument("--qa", action="store_true", help="Run Chrome QA inspector on readers")
    parser.add_argument("--canva", action="store_true", help="Export Canva bulk datasets and specs")
    parser.add_argument("--video", action="store_true", help="Generate video blueprints and 3D simulation")
    args = parser.parse_args()

    config = BookConfig()
    print("=" * 80)
    print(f"🕉️  Tantra Gyan Multi-Agent Publishing Suite")
    print(f"📖 Flagship Vol {config.flagship_volume}: {config.title_hi}")
    print(f"🌐 International: {config.title_en}")
    print("=" * 80)

    orchestrator = BookOrchestratorAgent(config)
    simplifier = FormulaSimplifierAgent()
    storyteller = LaymanStorytellerAgent()
    diagrammer = ChartDiagramGeneratorAgent()
    auditor = VisualAuthenticityAuditorAgent(config.project_root)
    qa_monitor = ChromeQAMonitorAgent(config.project_root)
    canva_agent = CanvaAssetAgent()
    video_agent = VideoConceptAgent()

    if args.plan or args.all or len(sys.argv) == 1:
        print("\n[Stage 1] Master Orchestrator Planning...")
        plan = orchestrator.plan_workflow()
        print(f"  ✓ Planned Chapters: {plan['total_chapters']}")
        for i, ch in enumerate(plan["chapters"], 1):
            print(f"    {i:02d}. {ch['title']} (Source: {ch['source']})")

    if args.audit or args.all:
        print("\n[Stage 2] Visual Authenticity Audit...")
        status = auditor.check_status()
        print(f"  ✓ Auditor Status: {status.get('status')}")
        det = auditor.run_detection()
        print(f"  ✓ Detection Completed: {det.get('total_findings', 0)} findings analyzed.")

    if args.qa or args.all:
        print("\n[Stage 3] Chrome QA & Asset Inspection...")
        for page in ["index.html", "reader.html", "bnn-reader.html", "sadhana-reader.html", "kundali-ganita.html", "kundali-ganita-reader.html"]:
            res = qa_monitor.inspect_html_file(page)
            print(f"  ✓ {page}: {res.get('status')} ({res.get('file_size_kb', 0)} KB)")

    if args.canva or args.all:
        print("\n[Stage 4] Canva Asset & Bulk Dataset Agent...")
        csv_file = canva_agent.generate_bulk_dataset()
        canva_spec = canva_agent.get_canva_spec()
        print(f"  ✓ Canva Folder: {canva_spec['canva_folder_name']} (ID: {canva_spec['canva_folder_id']})")
        print(f"  ✓ Bulk Dataset: {csv_file}")

    if args.video or args.all:
        print("\n[Stage 5] Video Concept & 3D Animation Agent...")
        bp_file = video_agent.generate_video_blueprints()
        anim_file = video_agent.generate_interactive_3d_animation()
        print(f"  ✓ Video Blueprints: {bp_file}")
        print(f"  ✓ 3D Simulation: {anim_file}")

    print("\n[Pipeline Complete] Multi-agent workflow execution verified.")
    print("=" * 80)


if __name__ == "__main__":
    main()
