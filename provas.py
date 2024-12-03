import flet as ft

def main(page: ft.Page):
    def envio(e):
        page.add(ft.Text("Formulário enviado com sucesso!"))
    
    def email():
        page.add(
            ft.Column([
                ft.Text("Nome:",size=15, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                ft.TextField(label="Digite o seu nome"),
                ft.Text("Email:",size=15, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                ft.TextField(label="Digite o seu email"),
                ft.Text("Mensagem:",size=15, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD),
                ft.TextField(label="Digite uma mensagem"),
                ft.ElevatedButton(text="Enviar", color="BLACK", on_click=envio),
                
            ])
        )
    email()

ft.app(target=main)