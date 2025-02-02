import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Kitchen(Node):
    def __init__(self):
        super().__init__('kitchen')
        self.subscription = self.create_subscription(String, '/orders', self.listener_callback, 10)
        self.publisher = self.create_publisher(String, '/food_ready', 10)

    def listener_callback(self, msg):
        table_name = msg.data  # Get the table name (e.g., table1, table2, table3)
        self.get_logger().info(f"Received order for {table_name}")
        
        # Simulate food preparation
        self.get_logger().info(f"Preparing food for {table_name}...")
        self.get_logger().info("Food is ready!")
        
        # Publish the food readiness
        food_ready_msg = String()
        food_ready_msg.data = table_name  # Pass the table name to the next step
        self.publisher.publish(food_ready_msg)

def main(args=None):
    rclpy.init(args=args)
    kitchen = Kitchen()
    rclpy.spin(kitchen)
    kitchen.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
