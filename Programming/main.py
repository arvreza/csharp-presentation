from manim import *
class DefaultTemplate(Scene):
    def construct(self):
        #self.what_is_programming()
        #self.programming_step_by_step()
        self.long_function_args()
        #self.single_responsibility()
        #self.what_is_prime()
        #self.is_prime()

    def what_is_programming(self):
        txt = Text('برنامه‌نویسی چیست؟', color=BLUE_B,slant=ITALIC, font="sans-serif") 
        self.play(Write(txt, reverse=True), run_time=10)

    def programming_step_by_step(self):
        dotCenter = LabeledDot(Tex('Step 2', color=BLACK), color=BLUE_B) 
        dotLeft = LabeledDot(Tex('Step 1', color=BLACK), color=BLUE_B) 
        dotRight = LabeledDot(Tex('Step 3', color=BLACK), color=BLUE_B) 
        arrowLeft = Arrow(color= BLUE_B) 
        arrowRight = Arrow(color= BLUE_B) 
        arrowLeft.next_to(dotCenter, LEFT)
        dotLeft.next_to(arrowLeft, LEFT)
        arrowRight.next_to(dotCenter)
        dotRight.next_to(arrowRight)

        group = VGroup(dotLeft, arrowLeft, dotCenter, arrowRight, dotRight)

        self.play(Create(group), run_time=12)

    def long_function_args(self):
        bad_code = Code("./resources/LongFunctionParams.cs", language="c#", font="Monospace", style='native')
        self.play(Create(bad_code))
        self.wait(4)

    def single_responsibility(self):
        bad_code = Code("./resources/CreateAndSortAndShuffle.cs", language="c#", font="Monospace", style='native')
        self.play(Create(bad_code))
        self.wait(4)

    def what_is_prime(self):
        txt = Text('  عدد اول عددی‌ست که\n تنها بر خود و یک قابل قسمت باشد', color=BLUE_B,slant=ITALIC, font="sans-serif") 
        self.play(Write(txt), run_time=10)

    def is_prime(self):
        txt = Text('bool IsPrime(int n)', color=GREEN_A,slant=ITALIC, font="sans-serif") 
        self.play(Write(txt), run_time=5)
