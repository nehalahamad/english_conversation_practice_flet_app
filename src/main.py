import flet as ft
import json



class Conversation:
    def __init__(self):
        pass

    def display(self, conversation):
        title = ft.Container(
            content=ft.Text(conversation["title"], size=15),
            bgcolor=ft.Colors.WHITE,
            padding=10,
            margin=5,
            border_radius=10,
            # expand=True,
            # width=360,
            alignment=ft.alignment.center
        )

        column = ft.Column()

        for line in conversation["lines"]:
            if 'S1.' in line:
                column.controls.append(
                    ft.Container(
                        content=ft.Text(line, size=12, color=ft.Colors.BLUE),
                        bgcolor=ft.Colors.WHITE,
                        alignment=ft.alignment.center_left,
                        border_radius=5,
                        padding=5,
                
                    )
                )
            elif 'S2.' in line:
                column.controls.append(
                    ft.Container(
                        content=(ft.Text(line, size=12, color=ft.Colors.RED)),
                        bgcolor=ft.Colors.WHITE,
                        alignment=ft.alignment.center_right,
                        border_radius=5,
                        padding=5
                    )
                )
        
        return ft.Column(
            # alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                title,
                column
            ]
        )
        

class Exercise:
    def __init__(self):
        pass

    def display(self, exercise):
        title = ft.Container(
            content=ft.Text(exercise["title"], size=15),
            bgcolor=ft.Colors.WHITE,
            padding=10,
            margin=5,
            border_radius=10,
            # expand=True,
            width=360,
            alignment=ft.alignment.center
        )
        example_sentence = ft.Container(
            content=ft.Text(exercise["example_sentence"], size=15),
            bgcolor=ft.Colors.WHITE,
            padding=10,
            margin=5,
            border_radius=10,
            # expand=True,
            width=360,
            alignment=ft.alignment.center
        )

        column = ft.Column(
            expand=2,
            scroll=True

        )
        for line in exercise["lines"]:
            word = line['word']
            sentence = line['sentence']
            column.controls.append(
                ft.Container(
                    content=ft.Text(word, size=12, color=ft.Colors.BLUE),
                    bgcolor=ft.Colors.WHITE,
                    alignment=ft.alignment.center_left,
                    border_radius=ft.border_radius.only(top_right=5, bottom_right=5),
                    padding=5
                )
            )
            column.controls.append(
                ft.Container(
                    content=ft.Text(sentence, size=12, color=ft.Colors.RED),
                    bgcolor=ft.Colors.WHITE,
                    alignment=ft.alignment.center_right,
                    border_radius=ft.border_radius.only(top_left=5, bottom_left=5),
                    padding=5
                )
            )
        return ft.Column(
            controls=[
                title,
                example_sentence,
                column
            ],
            # scroll=True
        )





# Load JSON data from a file
def load_json_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Load chapters data from a JSON file
english_conversation_practice = load_json_data("src/assets/english_conversation_practice_3ch.json")






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

        self.drawer = ft.NavigationDrawer(on_dismiss=self.handle_dismissal, on_change=self.handle_change, selected_index=0)
        
        self.current_conversations_list = english_conversation_practice[self.selected_chapter]["conversations"]
        self.current_exercises_list = english_conversation_practice[self.selected_chapter]["exercises"]

        self.current_conversation_exercise = 0
        self.conversation_exercise_list = self.get_conversation_exercise_list(self.current_conversations_list, self.current_exercises_list)

        self.conversation_exercise_widget = ft.Container(
            height=420, 
            # bgcolor=ft.Colors.RED, 
            padding=10, 
            border_radius=10
        )
        # self.conversation_exercise_widget.content=self.conversation_obj.display(self.current_conversations_list[self.current_conversation_exercise])
        self.conversation_exercise_widget.content=self.get_conversation_exercise_widget(self.current_conversations_list[self.current_conversation_exercise])



        self.appbar = ft.AppBar(
            leading=ft.IconButton(icon=ft.Icons.MENU, on_click=lambda e: self.page.open(self.drawer), data=0),
            leading_width=40,
            title=ft.Text(english_conversation_practice[self.selected_chapter]["chapter"], size=15),
            center_title=False,
            bgcolor=ft.Colors.GREEN_100,
            actions=[
                ft.IconButton(ft.Icons.ARROW_CIRCLE_RIGHT_OUTLINED, on_click=self.get_next_chapter)
            ]
        )
        self.page.appbar = self.appbar

        for chapter in english_conversation_practice:
            self.drawer.controls.append(
                ft.NavigationDrawerDestination(
                    label=chapter["chapter"]
                    )
            )

        self.page.add(self.conversation_exercise_widget)


        # addnig Prev, Next and Next Chapter buttons
        page.add(
            ft.Row(
                alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    ft.ElevatedButton("Prev", on_click=self.get_prev),
                    ft.ElevatedButton("Next", on_click=self.get_next)
                ]
            )
        )
        # page.add(ft.ElevatedButton("Next Chapter", on_click=self.get_next_chapter))
         
        page.update()




    def get_next(self, e):
        self.current_conversation_exercise += 1
        if self.current_conversation_exercise >= len(self.conversation_exercise_list):
            self.current_conversation_exercise = 0
        self.conversation_exercise_widget.content=self.get_conversation_exercise_widget(self.conversation_exercise_list[self.current_conversation_exercise])
        self.page.update()

    def get_prev(self, e):
        self.current_conversation_exercise -= 1
        if self.current_conversation_exercise < 0:
            self.current_conversation_exercise = len(self.conversation_exercise_list) - 1
        # self.conversation_exercise_widget.content=self.conversation_obj.display(        self.conversation_exercise_list[self.current_conversation_exercise])
        self.conversation_exercise_widget.content=self.get_conversation_exercise_widget(self.conversation_exercise_list[self.current_conversation_exercise])
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
        self.page.update()


    def handle_dismissal(self, e):
        self.selected_chapter = e.control.selected_index
        chapter = english_conversation_practice[e.control.selected_index]["chapter"]
        self.appbar.title = ft.Text(chapter, size=15)
        self.page.update()


    def handle_change(self, e):
        pass
        # chapter = english_conversation_practice[e.control.selected_index]["chapter"]
        # self.appbar.title = ft.Text(chapter, size=15)


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

ft.app(target=main)