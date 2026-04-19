from ..models.navigation import NavigationSpec

def project_nav_ascii(spec: NavigationSpec, width: int = 80) -> str:
    lines = []
    
    # Title
    title_str = f"┌─ {spec.title} "
    lines.append(title_str.ljust(width - 1, '─') + "┐")
    
    # Workspaces
    for ws in spec.workspaces:
        lines.append("│ " + f"[{ws.label}]".ljust(width - 4) + " │")
        
    # Routes
    if spec.routes:
        lines.append("├" + "─" * (width - 2) + "┤")
        for route in spec.routes:
            trigger_str = f" -> {route.trigger} -> " if route.trigger else " -> "
            route_str = f"{route.from_workspace}{trigger_str}{route.to_workspace}"
            lines.append("│ " + route_str.ljust(width - 4) + " │")
            
    # Rules
    if spec.rules:
        lines.append("├" + "─" * (width - 2) + "┤")
        rules_str = " | ".join(spec.rules)
        lines.append("│ " + rules_str.ljust(width - 4) + " │")
        
    # Footer
    lines.append("└" + "─" * (width - 2) + "┘")
    
    return "\n".join(lines)
