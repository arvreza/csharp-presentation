from cgitb import text
from lib2to3.pgen2.token import DOT
from tkinter import BOTTOM, TOP
from turtle import fillcolor, left, right
from cloup import Color
from manim import *

class DefaultTemplate(Scene):
    def construct(self):
        self.function_definition()
        self.clear()
        self.function_error()
        self.clear()
        self.try_catch_syntax()
        self.next_section()
        self.clear()
        self.exception_bubble_up()
        self.next_section()
        self.clear()
        self.using_syntax()
        self.next_section()
        self.clear()
        self.bad_code()
        self.next_section()
        self.clear()
        self.throwing_exceptions()
        self.next_section()
        self.clear()
        self.common_exceptions()

    def exception_bubble_up(self):      
        inner1 = Text("    تابع اصلی ", font="sans-serif", font_size=20)
        functionBox1 = VGroup(inner1, SurroundingRectangle(inner1, corner_radius=0.1, color=YELLOW, buff=0.5))
        functionBox1.shift(3 * UP)
        downArrow1 = Arrow(stroke_width=4, start=DOWN, end=config.bottom*0.5, buff=0.25) 
        downArrow1.next_to(functionBox1, DOWN)

        inner2 = Text("    تابع فرعی یک ", font="sans-serif", font_size=20)
        functionBox2 = VGroup(inner2, SurroundingRectangle(inner2, corner_radius=0.1, color=YELLOW, buff=0.5))
        functionBox2.next_to(downArrow1, DOWN)
        downArrow2 = Arrow(stroke_width=4, start=DOWN, end=config.bottom*0.5, buff=0.25) 
        downArrow2.next_to(functionBox2, DOWN)

        inner3 = Text("    تابع فرعی دو ", font="sans-serif", font_size=20, color=RED, weight=BOLD)
        functionBox3 = VGroup(inner3, SurroundingRectangle(inner3, corner_radius=0.1, color=YELLOW, buff=0.5))
        functionBox3.next_to(downArrow2, DOWN)

        self.play(Create(functionBox1), Create(downArrow1), Create(functionBox2), Create(downArrow2), Create(functionBox3))
        self.wait(2)

        for x in range(3):
            self.play(Flash(inner3, 
                line_length=1, 
                num_lines=30, 
                color=RED, 
                flash_radius=2, 
                time_width=0.3, 
                run_time=2))
        self.wait(2)
 
        errorArrow1 = CurvedArrow(DOWN,UP, color=RED) 
        errorArrow1.next_to(functionBox3, RIGHT).shift(UP)

        errorArrow2 = CurvedArrow(DOWN,UP, color=RED) 
        errorArrow2.next_to(functionBox2, RIGHT).shift(UP)

        self.play(Create(errorArrow1))
        self.play(Create(errorArrow2))
        self.wait(2)

    def function_definition(self):
        inner = Text("    تابع", font="sans-serif")
        self.play(Write(inner))
        functionBox = SurroundingRectangle(inner, corner_radius=0.1, buff=1, color=WHITE) 
        self.play(Create(functionBox))
        self.wait(2)

        leftArrow = Arrow(stroke_width=4, color= WHITE) 
        leftArrow.next_to(functionBox, LEFT, 1)

        rightArrow = Arrow(stroke_width=4, color= WHITE) 
        rightArrow.next_to(functionBox, RIGHT, 1)
        self.add(leftArrow, rightArrow)

        topDot = Dot(ORIGIN, color=YELLOW)
        leftDot = Dot(LEFT, color=GREEN).shift(0.1*DOWN + 0.5*RIGHT)
        rightDot = Dot(RIGHT, color=RED).shift(0.1*DOWN + 0.5*LEFT)
        inputs = VGroup(leftDot, topDot, rightDot).scale(1.5)
        inputs.next_to(functionBox, LEFT, 3)
        self.add(inputs)
        self.wait(2)
        self.play(Transform(inputs, functionBox))
        self.wait(2)
        output = Dot(color=WHITE)
        output.next_to(rightArrow, RIGHT).scale(1.8)
        self.play(FadeIn(output))
        self.wait(2)
    
    def function_error(self):
        inner = Text("    تابع", font="sans-serif")
        self.play(Write(inner))
        functionBox = SurroundingRectangle(inner, corner_radius=0.1, buff=1, color=WHITE) 
        self.play(Create(functionBox))
        self.wait(1)

        leftArrow = Arrow(stroke_width=4, color= WHITE) 
        leftArrow.next_to(functionBox, LEFT, 1)

        rightArrow = Arrow(stroke_width=4, color= WHITE) 
        rightArrow.next_to(functionBox, RIGHT, 1)
        self.add(leftArrow, rightArrow)

        topDot = Dot(ORIGIN, color=YELLOW)
        leftDot = Dot(LEFT, color=GREEN).shift(0.1*DOWN + 0.5*RIGHT)
        rightDot = Dot(RIGHT, color=RED).shift(0.1*DOWN + 0.5*LEFT)
        inputs = VGroup(leftDot, topDot, rightDot).scale(1.5)
        inputs.next_to(functionBox, LEFT, 3)
        self.add(inputs)
        self.wait(1)
        self.play(Transform(inputs, functionBox))
        self.wait(1)
        self.remove(inner)
        innerError = Text("    تابع", font="sans-serif", color=RED, weight=BOLD)
        self.add(innerError)
        self.remove(rightArrow)
        
        for x in range(3):
            self.play(Flash(innerError, 
                line_length=1, 
                num_lines=30, 
                color=RED, 
                flash_radius=2, 
                time_width=0.3, 
                run_time=2))
        self.wait(1)
    
    def try_catch_syntax(self):
        rendered_code = Code("./resources/TryCatch.cs", language="c#", font="Monospace", style=Code.styles_list[15])
        self.play(Create(rendered_code))
        self.wait(1)
        
    def using_syntax(self):
        verbose_code = Code("./resources/ReadFile.cs", language="c#", font="Monospace", style='native')
        self.play(Create(verbose_code))
        self.wait(4)
        using_syntax = Code("./resources/ReadFileUsing.cs", language="c#", font="Monospace", style='native')
        self.play(Transform(verbose_code, using_syntax))
        self.wait(4)

    def bad_code(self):
        bad_code = Code("./resources/CatchAll.cs", language="c#", font="Monospace", style='native')
        self.play(Create(bad_code))
        self.wait(4)
        cross = Cross(stroke_color = RED, stroke_width=10) 
        self.play(Create(cross))

    def throwing_exceptions(self):
        throw_code = Code("./resources/ThrowExceptions.cs", language="c#", font="Monospace", style='native')
        self.play(Create(throw_code))
        self.wait(4)
        throw_code_opt = Code("./resources/ThrowExceptions1.cs", language="c#", font="Monospace", style='native')
        self.play(Transform(throw_code, throw_code_opt))
        self.wait(4)

    def common_exceptions(self):
        text = Text("از این کلاس در زمانی استفاده می‌کنیم\n که آرگومان‌های اشتباه به تابع داده شده‌اند", 
        font="sans-serif", 
        font_size=28,
        line_spacing=1.5,
        color=YELLOW)

        code = Code(code="System.ArgumentExceptions", language="c#", font="Monospace", style='native', insert_line_no=False)
        code.next_to(text, UP)
        self.play(Create(code))
        self.play(Write(text))
        self.wait(3)

        self.clear()

        text = Text("از این کلاس در زمانی استفاده می‌کنیم\n که آرگومان‌ها با محتوای خالی به تابع داده شده‌اند", 
        font="sans-serif", 
        font_size=28,
        line_spacing=1.5,
        color=YELLOW)

        code = Code(code="System.ArgumentNullExceptions", language="c#", font="Monospace", style='native', insert_line_no=False)
        code.next_to(text, UP)
        self.play(Create(code))
        self.play(Write(text))
        self.wait(3)

        self.clear()

        text = Text("از این کلاس در زمانی استفاده می‌کنیم\n که آرگومان‌هایی که به تابع داده شده‌اند\n یا زیادی بزرگ هستند یا زیادی کوچک", 
        font="sans-serif", 
        font_size=28,
        line_spacing=1.5,
        color=YELLOW)

        code = Code(code="System.ArgumentOutOfRangeException", language="c#", font="Monospace", style='native', insert_line_no=False)
        code.next_to(text, UP)
        self.play(Create(code))
        self.play(Write(text))
        self.wait(3)

        self.clear()

        text = Text("از این کلاس در زمانی استفاده می‌کنیم\n که شرایط یک آبجکت در تابع اجازه ادامه دادن برنامه را نمی‌دهد\n مثال: خواندن یک عضوی از لیست که محتوای آن قبل از شروع تابع تغییر کرده‌است ", 
        font="sans-serif", 
        font_size=28,
        line_spacing=1.5,
        color=YELLOW)

        code = Code(code="System.InvalidOperationException", language="c#", font="Monospace", style='native', insert_line_no=False)
        code.next_to(text, UP)
        self.play(Create(code))
        self.play(Write(text))
        self.wait(3)

        self.clear()
        text = Text("از این کلاس در زمانی استفاده می‌کنیم\nکه عمل ناممکن از تابع درخواست شده است \n مثال: اضافه کردن به لیستی که نوشتن بر آن ممکن نیست ", 
        font="sans-serif", 
        font_size=28,
        line_spacing=1.5,
        color=YELLOW)

        code = Code(code="System.InvalidOperationException", language="c#", font="Monospace", style='native', insert_line_no=False)
        code.next_to(text, UP)
        self.play(Create(code))
        self.play(Write(text))
        self.wait(3)
