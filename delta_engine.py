import os
import time
import sys
from rich.console import Console
from rich.panel import Panel
from rich.progress import track
from rich.text import Text

console = Console()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    banner = """
    ██████╗ ███████╗██╗     ████████╗ █████╗ 
    ██╔══██╗██╔════╝██║     ╚══██╔══╝██╔══██╗
    ██║  ██║█████╗  ██║        ██║   ███████║
    ██║  ██║██╔══╝  ██║        ██║   ██╔══██║
    ██████╔╝███████╗███████╗   ██║   ██║  ██║
    ╚═════╝ ╚══════╝╚══════╝   ╚═╝   ╚═╝  ╚═╝
    """
    console.print(Panel(Text(banner, style="bold blue", justify="center"), title="[bold cyan]v2.0.4 | Python Engine[/]", border_style="cyan"))

def attach_process():
    console.print("[yellow]Scanning for Roblox process...[/yellow]")
    time.sleep(1.5)
    for _ in track(range(100), description="[green]Injecting API..."):
        time.sleep(0.02)
    console.print("\n[bold green][+] Successfully attached to Roblox![/bold green]")
    console.print("[dim]API initialized. Ready for execution.[/dim]\n")

def main():
    clear_screen()
    print_banner()
    console.print("Type [bold green]'help'[/bold green] for a list of commands.\n")
    
    is_attached = False

    while True:
        try:
            command = console.input("[bold cyan]Delta[/bold cyan][bold white]>[/bold white] ").strip()
            
            if not command:
                continue
                
            parts = command.split(" ", 1)
            cmd = parts[0].lower()
            args = parts[1] if len(parts) > 1 else ""

            if cmd == "help":
                console.print("\n[bold]Available Commands:[/bold]")
                console.print("  [cyan]inject[/cyan]   - Attach the executor to the game process")
                console.print("  [cyan]exec[/cyan]     - Execute a Lua script (e.g., exec print('hello'))")
                console.print("  [cyan]clear[/cyan]    - Clear the terminal screen")
                console.print("  [cyan]exit[/cyan]     - Close Delta Executor\n")
            
            elif cmd == "inject":
                if is_attached:
                    console.print("[yellow][!] Already attached to process.[/yellow]")
                else:
                    attach_process()
                    is_attached = True
                    
            elif cmd == "exec":
                if not is_attached:
                    console.print("[red][X] Error: You must 'inject' first![/red]")
                elif not args:
                    console.print("[red][X] Error: Please provide a script to execute.[/red]")
                else:
                    console.print(f"[dim]Executing payload ({len(args)} bytes)...[/dim]")
                    time.sleep(0.5)
                    console.print("[bold green][+] Execution successful![/bold green]")
                    
            elif cmd == "clear":
                clear_screen()
                print_banner()
                
            elif cmd in ["exit", "quit"]:
                console.print("[yellow]Shutting down Delta Engine...[/yellow]")
                time.sleep(0.5)
                sys.exit(0)
                
            else:
                console.print(f"[red]Unknown command: '{cmd}'. Type 'help' for options.[/red]")
                
        except KeyboardInterrupt:
            console.print("\n[yellow]Shutting down...[/yellow]")
            sys.exit(0)

if __name__ == "__main__":
    main()
