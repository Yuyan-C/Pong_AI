# Author(s): Yueting Chen Yuyan Chen
# McGill ID(s): 260918307 260883741
# Pong AI Project

class PongAI:
    def __init__(self, table_size):
        """
        table_size --   A tuple representing the dimensions of the table.
                        The x and y dimensions of the table are represented by
                                    table_size[0], table_size[1]
                        respectively.
        """
        self.table_size = table_size
        self.trace=[] # to store the position of the ball
        
        # add code here if you like
        # (to store data between calls to the method)

    def pong_ai(self, paddle_rect, other_paddle_rect, ball_rect):
        """Return "up" or "down", depending on which way the paddle should go to
        align its centre with the centre of the ball
   
        Keyword arguments:
        paddle_rect -- A rectangle object representing the coordinates of your paddle.
                       The top-left corner of the rectangle is represented by the tuple
                                    paddle_rect.pos[0], paddle_rect.pos[1]
                       The dimensions (width, height) of the paddle are represented by
                                    paddle_rect.size[0], paddle_rect.size[1]
    
        other_paddle_rect -- A rectangle representing the opponent's paddle.
                        It is the same kind of object as above and its attributes
                        can be accessed in the same manner described above.
   
        ball_rect --    A rectangle representing the ball. It is the same kind of object
                        as the two above.
   
        Coordinates start at (0, 0) in the top-left corner.
        They look as follows:
   
   
                0             x
                |------------->
                |
                |             
                |
            y   v
        """
        if len(self.trace)<2:
            self.trace.append(ball_rect.pos)
        else:
            self.trace.remove(self.trace[0])
            self.trace.append(ball_rect.pos)
            x1=self.trace[1][0]
            x0=self.trace[0][0]
            y1=self.trace[1][1]
            y0=self.trace[0][1]
            dx=x1-x0
            dy=y1-y0
            # find the expression for y: y = slope*x + y_int
            if dx==0:
                return None
            slope = dy/dx
            y_int = y0 - slope*x0
            
            if paddle_rect.pos[0]> 0.5*self.table_size[0]: # if the paddle is on the right side
                
                if x1>x0: # if the ball is facing towards the paddle
                    
                    fut_x = paddle_rect.pos[0]
                    fut_y = slope*fut_x + y_int
                    
                    n = 0
                    while n< 100 and (fut_y<0 or fut_y>self.table_size[1]): # if the ball cannot hit the right side of the wall directly 
                       
                       if fut_y<0 and slope != 0: # if the ball will hit the top side of the table
                           refp=(-y_int/slope,0) # calculate the reflection point
                          
                           x=refp[0]
                           y=refp[1]
                           slope=-slope
                           y_int=y-slope*(x)
                           fut_y=slope*fut_x+y_int

                       if fut_y> self.table_size[1] and slope !=0: # if the ball will hit the bottom side of the table 
                           refp=((self.table_size[1]-y_int)/slope,self.table_size[1]) # calculate the reflection point
                       
                           x=refp[0]
                           y=refp[1]
                           slope=-slope
                           y_int=y-slope*(x)
                           fut_y=slope*fut_x+y_int
                        
                       n += 1
                      
                       
                    if fut_y > 0 and fut_y < self.table_size[1]:
                    
                        if paddle_rect.pos[1]+paddle_rect.size[1]/2>fut_y+ball_rect.size[1]/2:
                            return"up"
                        else:
                            return"down"
                        
                    else:
                        if paddle_rect.pos[1]+0.5*(paddle_rect.size[1])>0.5*self.table_size[1]:
                            return"up"
                        else:
                            return"down"
                
                        
                else:
                    if paddle_rect.pos[1]+0.5*(paddle_rect.size[1])>0.5*self.table_size[1]:
                        return"up"
                    else:
                        return"down"
                
                    
            if paddle_rect.pos[0]< 0.5*self.table_size[0]: # if the paddle is on the left side
                
                if x1<x0: # if the ball is facing towards the paddle
                    
                    fut_x = paddle_rect.pos[0]
                    fut_y = slope*fut_x + y_int
                    
                    n = 0
                    while n < 100 and (fut_y<0 or fut_y>self.table_size[1]): # if the ball cannot hit the right side of the wall directly 
                       
                       if fut_y<0 and slope != 0: # if the ball will hit the top side of the table
                           refp=(-y_int/slope,0) # calculate the reflection point

                           x=refp[0]
                           y=refp[1]
                           slope=-slope
                           y_int=y-slope*(x)
                           fut_y=slope*fut_x+y_int

                       if fut_y> self.table_size[1] and slope != 0: # if the ball will hit the bottom side of the table 
                           refp=((self.table_size[1]-y_int)/slope,self.table_size[1]) # calculate the reflection point
                       
                           x=refp[0]
                           y=refp[1]
                           slope=-slope
                           y_int=y-slope*(x)
                           fut_y=slope*fut_x+y_int
                           
                       n += 1
                    if fut_y > 0 and fut_y < self.table_size[1]:
                    
                        if paddle_rect.pos[1]+paddle_rect.size[1]/2>fut_y+ball_rect.size[1]/2:
                            return"up"
                        else:
                            return"down"
                        
                    else:
                        if paddle_rect.pos[1]+0.5*(paddle_rect.size[1])>0.5*self.table_size[1]:
                            return"up"
                        else:
                            return"down"
                
                        
                else:
                    if paddle_rect.pos[1]+0.5*(paddle_rect.size[1])>0.5*self.table_size[1]:
                        return"up"
                    else:
                        return"down"
                
                       
                       
                       
                       
                       
                       
                    
            
        
    
