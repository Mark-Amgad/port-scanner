import typer
from .models import ScanConfig
from .scanner import scan_ports
from rich import print

app = typer.Typer()


@app.command()
def scan(
    host: str = typer.Option(
        ..., "--host", "-h", help="Target IP address or hostname."
    ),
    start_port: int = 1,
    end_port: int = 1024,
    timeout: float = 1.0,
):
    try:
        config = ScanConfig(
            host=host, start_port=start_port, end_port=end_port, timeout=timeout
        )
        open_ports = scan_ports(config)
        if open_ports:
            print(f"[green]Open ports:[/green] {open_ports}")
        else:
            print("[yellow]No open ports found[/yellow]")
    except Exception as e:
        print(f"[red]Error:[/red] {e}")


if __name__ == "__main__":
    app()
