# rcj_soccer_player controller - ROBOT B1

# Feel free to import built-in libraries
from cmath import pi
import math

# You can also import scripts that you put into the folder with controller
import utils
from rcj_soccer_robot import RCJSoccerRobot, TIME_STEP


class MyRobot1(RCJSoccerRobot):
    def run(self):
        
        x=-0.45
        
        while self.robot.step(TIME_STEP) != -1:
            if self.is_new_data():
                data = self.get_new_data()  # noqa: F841

                while self.is_new_team_data():
                    team_data = self.get_new_team_data()  # noqa: F841
                    # Do something with team data

                if self.is_new_ball_data():
                    ball_data = self.get_new_ball_data()
                ''' else:
                    # If the robot does not see the ball, stop motors
                    self.left_motor.setVelocity(0)
                    self.right_motor.setVelocity(0)
                    continue'''

                # Get data from compass
                heading = self.get_compass_heading()  # noqa: F841
                robot_pos = self.get_gps_coordinates()  # noqa: F841
                
                kp=5
                ex=ball_data['direction'][0]-robot_pos[1]
                
                print(ball_data)
                
                self.left_motor.setVelocity(kp*ex)
                self.right_motor.setVelocity(kp*ex)
                
                if(abs(ex)<0.5):
                 
                    rd=3.14/2
                    er=ball_data['strength']-heading
                    self.left_motor.setVelocity(3*kp*er)
                    self.right_motor.setVelocity(-3*kp*er)
                    if(abs(er)<0.1):
                       y=-0.7
                       ey=ball_data['direction'][1]-robot_pos[0]
                       self.left_motor.setVelocity(-kp*ey)
                       self.right_motor.setVelocity(-kp*ey)
                      

                    
                    

                
                '''x=-0.37
                x0= robot_pos[1]
                errx=x0-x       
                kp=10
                sonar_values = self.get_sonar_values()  # noqa: F841
                #print(err)
                self.left_motor.setVelocity(kp*errx)
                self.right_motor.setVelocity(kp*errx)
                #print(errx)

                if(abs(errx)<0.1) : 
                    fi=heading
                    des=3.14/2
                    k=5
                    erofi=des - fi
                    #print(heading)
                    #print(erofi)
                    #self.left_motor.setVelocity(k*ero)
                    self.left_motor.setVelocity(k*erofi)
                    self.right_motor.setVelocity(0)  
                    if (abs(erofi) <0.1) :
                        y=-0.8
                        y0= robot_pos[0]
                        erry=y0-y       
                        kpp=7
                        sonar_values = self.get_sonar_values()  # noqa: F841
                    #print(err)                            self.left_motor.setVelocity(kpp*erry)
                        self.right_motor.setVelocity(kpp*erry)'''
                

                
                
                

                '''# Compute the speed for motors
                direction = utils.get_direction(ball_data["direction"])

                # If the robot has the ball right in front of it, go forward,
                # rotate otherwise
                if direction == 0:
                    left_speed = 7
                    right_speed = 7
                else:
                    left_speed = direction * 4
                    right_speed = direction * -4

                # Set the speed to motors
                self.left_motor.setVelocity(left_speed)
                self.right_motor.setVelocity(right_speed)

                # Send message to team robots
                self.send_data_to_team(self.player_id)'''