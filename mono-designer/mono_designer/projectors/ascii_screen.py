from ..models.screen import ScreenSpec

def project_screen_ascii(spec: ScreenSpec, width: int = 80) -> str:
    """
    Projects a ScreenSpec into an ASCII wireframe.
    """
    lines = []
    
    # 1. Header
    lines.append("┌" + "─" * (width - 2) + "┐")
    header_title = f" {spec.title} ({spec.id}) "
    lines.append("│" + header_title.center(width - 2) + "│")
    lines.append("├" + "─" * (width - 2) + "┤")
    
    # 2. Body Regions (Simplified for 0.3.0: vertical stack for now, or side-by-side if simple)
    # For now, let's do a vertical stack of regions to ensure stability
    for region in spec.regions:
        if region.type == "footer":
            continue
            
        lines.append("│ " + f"[{region.id.upper()}] {region.role}".ljust(width - 4) + " │")
        
        # Find components for this region
        comps = [c for c in spec.components if c.region == region.id]
        for comp in comps:
            lines.append("│   " + f"• {comp.id} ({comp.type}): {comp.purpose}".ljust(width - 6) + " │")
        
        lines.append("│" + " " * (width - 2) + "│")

    # 3. Actions / Transitions Hints (if any)
    if spec.actions:
        lines.append("├" + "─" * (width - 2) + "┤")
        lines.append("│ ACTIONS: " + ", ".join([a.label for a in spec.actions]).ljust(width - 11) + " │")

    # 4. Footer Key Strip
    lines.append("├" + "─" * (width - 2) + "┤")
    if spec.footer_keys:
        key_strip = " ".join([f"[{k.key}] {k.label}" for k in spec.footer_keys])
        lines.append("│ " + key_strip.ljust(width - 4) + " │")
    else:
        lines.append("│" + " " * (width - 2) + "│")
        
    lines.append("└" + "─" * (width - 2) + "┘")
    
    return "\n".join(lines)
