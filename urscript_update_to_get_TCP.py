import rtde_receive
import time

# UR5 robot's IP address
robot_ip = "192.168.1.102"  # Replace with your robot's actual IP address

# Create an RTDE receive interface to receive data from the robot
rtde_r = rtde_receive.RTDEReceiveInterface(robot_ip)

try:
    while True:
        # Get the current TCP position (X, Y, Z, RX, RY, RZ)
        tcp_pose = rtde_r.getActualTCPPose()

        # Print TCP position
        print("TCP Position: X: {:.3f}, Y: {:.3f}, Z: {:.3f}, RX: {:.3f}, RY: {:.3f}, RZ: {:.3f}".format(
            tcp_pose[0], tcp_pose[1], tcp_pose[2], tcp_pose[3], tcp_pose[4], tcp_pose[5]
        ))

        # Sleep for a short time to control the rate of data retrieval
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Program interrupted and stopped.")
