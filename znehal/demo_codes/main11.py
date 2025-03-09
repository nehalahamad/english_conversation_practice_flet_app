import flet as ft
from controls.my_conversation import Conversation
from controls.my_exercise import Exercise
from controls.custom_progressbar import CustomProgressBar
from my_utility.my_functions import load_json_data



class MyAppBar:
    def __init__(self):
        pass

english_conversation_practice = load_json_data("src/assets/english_conversation_practice.json")



class MyApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.scroll = True
        self.page.bgcolor = ft.Colors.GREY_200
        self.page.title = "English Conversation Practice"
        # self.page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.page.window.width = 360
        self.page.window.height = 640
        self.selected_index = 0
        self.selected_chapter = 0

        self.conversation_obj = Conversation()
        self.exercise_obj = Exercise()

        self.drawer = ft.NavigationDrawer(
            on_dismiss=self.handle_dismissal, 
            on_change=self.handle_change, 
            selected_index=0
        )
        
        self.current_conversations_list = english_conversation_practice[self.selected_chapter]["conversations"]
        self.current_exercises_list = english_conversation_practice[self.selected_chapter]["exercises"]
        self.conversation_exercise_list = self.get_conversation_exercise_list(self.current_conversations_list, self.current_exercises_list)
        self.current_conversation_exercise = 0

        self.pb = ft.ProgressBar(
            value = (self.current_conversation_exercise + 1) / len(self.conversation_exercise_list),
            color='#3de5eb'
        )
        # self.pb = CustomProgressBar(
        #     len(self.current_conversations_list), len(self.current_exercises_list),
        #     value = ((self.current_conversation_exercise + 1) / len(self.conversation_exercise_list)),
        # )

        self.conversation_exercise_widget = ft.Container(
            height=480, 
            padding=10, 
            border_radius=10
        )
        self.conversation_exercise_widget.content=self.get_conversation_exercise_widget(self.current_conversations_list[self.current_conversation_exercise])


        # ---------------------------------------------------------------------------------------
        self.appbar = ft.AppBar(
            leading=ft.IconButton(icon=ft.Icons.MENU, on_click=lambda e: self.page.open(self.drawer), data=0),
            leading_width=40,
            title=ft.Text(english_conversation_practice[self.selected_chapter]["chapter"], size=15),
            center_title=False,
            bgcolor='#06b7bd',
            actions=[
                ft.IconButton(ft.Icons.ARROW_CIRCLE_LEFT_OUTLINED, on_click=self.get_previous_chapter),
                ft.IconButton(ft.Icons.ARROW_CIRCLE_RIGHT_OUTLINED, on_click=self.get_next_chapter),
            ]
        )
        self.page.appbar = self.appbar

        # ---------------------------------------------------------------------------------------
        for chapter in english_conversation_practice:
            self.drawer.controls.append(
                ft.NavigationDrawerDestination(
                    label=chapter["chapter"]
                    )
            )
        # ---------------------------------------------------------------------------------------
        
        self.page.add(self.pb)
        self.page.add(self.conversation_exercise_widget)


        # addnig Prev, Next and Next Chapter buttons
        page.add(
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_AROUND,
                controls=[
                    ft.ElevatedButton("Prev", on_click=self.get_prev),
                    ft.ElevatedButton("Next", on_click=self.get_next)
                ]
            )
        )
         
        page.update()




    def get_next(self, e):
        self.current_conversation_exercise += 1
        if self.current_conversation_exercise >= len(self.conversation_exercise_list):
            self.current_conversation_exercise = 0
        self.conversation_exercise_widget.content=self.get_conversation_exercise_widget(self.conversation_exercise_list[self.current_conversation_exercise])
        self.pb.value = (self.current_conversation_exercise + 1) / len(self.conversation_exercise_list)
        self.page.update()

    def get_prev(self, e):
        self.current_conversation_exercise -= 1
        if self.current_conversation_exercise < 0:
            self.current_conversation_exercise = len(self.conversation_exercise_list) - 1
        self.conversation_exercise_widget.content=self.get_conversation_exercise_widget(self.conversation_exercise_list[self.current_conversation_exercise])
        self.pb.value = (self.current_conversation_exercise + 1) / len(self.conversation_exercise_list)
        self.page.update() 


    def get_next_chapter(self, e):
        self.selected_chapter += 1
        if self.selected_chapter >= len(english_conversation_practice):
            self.selected_chapter = 0
        self.current_conversations_list = english_conversation_practice[self.selected_chapter]["conversations"]
        self.current_exercises_list = english_conversation_practice[self.selected_chapter]["exercises"]
        
        self.current_conversation_exercise = 0
        self.conversation_exercise_list = self.get_conversation_exercise_list(self.current_conversations_list, self.current_exercises_list)

        self.conversation_exercise_widget.content=self.get_conversation_exercise_widget(self.conversation_exercise_list[self.current_conversation_exercise])
        self.appbar.title = ft.Text(english_conversation_practice[self.selected_chapter]["chapter"], size=15)
        self.drawer.selected_index = self.selected_chapter
        self.pb.value = (self.current_conversation_exercise + 1) / len(self.conversation_exercise_list)
        self.page.update()
    
    def get_previous_chapter(self, e):
        self.selected_chapter -= 1
        if self.selected_chapter < 0:
            self.selected_chapter = len(english_conversation_practice) - 1
        self.current_conversations_list = english_conversation_practice[self.selected_chapter]["conversations"]
        self.current_exercises_list = english_conversation_practice[self.selected_chapter]["exercises"]
        
        self.current_conversation_exercise = 0
        self.conversation_exercise_list = self.get_conversation_exercise_list(self.current_conversations_list, self.current_exercises_list)

        self.conversation_exercise_widget.content=self.get_conversation_exercise_widget(self.conversation_exercise_list[self.current_conversation_exercise])
        self.appbar.title = ft.Text(english_conversation_practice[self.selected_chapter]["chapter"], size=15)
        self.pb.value = (self.current_conversation_exercise + 1) / len(self.conversation_exercise_list)
        self.page.update()


    def handle_dismissal(self, e):
        self.selected_chapter = e.control.selected_index
        self.current_conversations_list = english_conversation_practice[self.selected_chapter]["conversations"]
        self.current_exercises_list = english_conversation_practice[self.selected_chapter]["exercises"]
        
        self.current_conversation_exercise = 0
        self.conversation_exercise_list = self.get_conversation_exercise_list(self.current_conversations_list, self.current_exercises_list)

        self.conversation_exercise_widget.content=self.get_conversation_exercise_widget(self.conversation_exercise_list[self.current_conversation_exercise])
        self.appbar.title = ft.Text(english_conversation_practice[self.selected_chapter]["chapter"], size=15)
        self.pb.value = (self.current_conversation_exercise + 1) / len(self.conversation_exercise_list)
        self.page.update()


    def handle_change(self, e):
        pass


    def get_conversation_exercise_list(self, conversations, exercises):
        conversation_exercise_list = []
        for i in range(len(conversations)):
            conv = conversations[i]
            conv['type'] = 'conversation'
            conversation_exercise_list.append(conv)
        
        for i in range(len(exercises)):
            ex = exercises[i]
            ex['type'] = 'exercise'
            conversation_exercise_list.append(ex)
        return conversation_exercise_list
    
    def get_conversation_exercise_widget(self, conversation_exercise):
        if conversation_exercise['type'] == 'conversation':
            return self.conversation_obj.display(conversation_exercise)
        elif conversation_exercise['type'] == 'exercise':
            return self.exercise_obj.display(conversation_exercise)


    

    



def main(page: ft.Page):
    MyApp(page)

ft.app(target=main, view=ft.AppView.WEB_BROWSER)