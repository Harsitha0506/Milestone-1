import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Table(Node):
    def __init__(self):
        super().__init__('table')
        self.subscription = self.create_subscription(String, '/food_ready', self.listener_callback, 10)

    def listener_callback(self, msg):
        table_name = msg.data  # Get the table name (e.g., table1, table2, table3)
        self.get_logger().info(f"Food delivered to {table_name}")

def main(args=None):
    rclpy.init(args=args)
    table = Table()
    rclpy.spin(table)
    table.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
