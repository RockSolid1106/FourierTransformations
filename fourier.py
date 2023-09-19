from manim import *
import cmath
p=75
SCALE=25
class fourier(MovingCameraScene):
    

    
    def construct(self):
        
        self.play(
            self.camera.frame.animate.scale(SCALE)
        )
        self.camera.frame_rate
        tracker = ValueTracker(0)
        self.add(tracker)
        
        c_pos = # Paste here the output of generate_coefficients.py, the first list
        c_neg = # the second list here
        arrows_pos = list()
        arrows_neg = list()
        
        def e2m(a):
            list = [a.real, a.imag, 0]
            return list
        
        def create_vecs(n):
            
            arrows_pos.append(Arrow(start=ORIGIN, end=e2m(c_pos[0]*cmath.exp(0*2*PI*1j*tracker.get_value())), buff=0))
            arrows_neg.append(Arrow(start=ORIGIN, end=e2m(c_neg[0]*cmath.exp(0*2*PI*1j*tracker.get_value())), buff=0))
            self.add(arrows_pos[0])

            for i in range(1, n):
                arrows_pos.append(Arrow(start=arrows_neg[i-1].get_end(), end=arrows_neg[i-1].get_end() + e2m(c_pos[i]*cmath.exp(float(i)*2*PI*1j*tracker.get_value())), buff=0))
                self.add(arrows_pos[i])
                
                arrows_neg.append(Arrow(start=arrows_pos[i].get_end(), end=arrows_pos[i].get_end() + e2m(c_neg[i]*cmath.exp(-float(i)*2*PI*1j*tracker.get_value())), buff=0))
                self.add(arrows_neg[i])
 
        def add_upd(n):
            arrows_pos[0].add_updater(
                lambda x: x.put_start_and_end_on(start=ORIGIN, end=e2m(c_pos[0]*cmath.exp(0*2*PI*1j*tracker.get_value())))
            )
            for i in range(1, n):
                arrows_pos[i].add_updater(
                    lambda x, i=i: x.put_start_and_end_on(start=arrows_neg[i-1].get_end(), end=arrows_neg[i-1].get_end() + e2m(c_pos[i]*cmath.exp(float(i)*2*PI*1j*tracker.get_value()))) # i=i because for each loop run, i gets overwritten
                )
            for i in range(1, n):
                arrows_neg[i].add_updater(
                    lambda x, i=i: x.put_start_and_end_on(start=arrows_pos[i].get_end(), end=arrows_pos[i].get_end() + e2m(c_neg[i]*cmath.exp(-float(i)*2*PI*1j*tracker.get_value()))) # i=i because for each loop run, i gets overwritten
                )
            
            

        create_vecs(p)
        add_upd(p)
        
        tracer = Dot(np.array(arrows_neg[p-1].get_end()), color=GREEN)
        trace = TracedPath(tracer.get_center, stroke_color=RED, stroke_width=25)
        self.add(tracer, trace) #tracer
        tracer.add_updater(
            lambda x: x.move_to(np.array(arrows_neg[p-1].get_end()))
        )
        

        tracker.add_updater(lambda x, dt: x.increment_value(dt*0.05))
        self.wait(25)
