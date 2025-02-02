import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class SiffleBot(Node):
    def __init__(self):
        super().__init__('siffle_bot')
        self.subscription = self.create_subscription(String, '/orders', self.listener_callback, 10)
        self.kitchen_sub = self.create_subscription(String, '/food_ready', self.kitchen_callback, 10)
        self.current_task = None

    def listener_callback(self, msg):
        table_name = msg.data  # Get the table name (e.g., table1, table2, table3)
        self.get_logger().info(f"Received order for {table_name}")
        self.current_task = table_name
        self.get_logger().info("Moving to kitchen...")
        # Simulate moving to kitchen

    def kitchen_callback(self, msg):
        if self.current_task == msg.data:
            table_name = msg.data  # Get the table name (e.g., table1, table2, table3)
            self.get_logger().info(f"Food ready for {table_name}. Moving to table...")
            # Simulate moving to table
            self.get_logger().info(f"Food delivered to {table_name}. Returning home.")
            self.current_task = None

def main(args=None):
    rclpy.init(args=args)
    siffle_bot = SiffleBot()
    rclpy.spin(siffle_bot)
    siffle_bot.destroy_node()
    rclpy.shutdown()

if __name__== '__main__':
    main()
