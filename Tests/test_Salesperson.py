from Models.User import User 

class Salesperson(User):
    def __init__(self, username, password, email=None, sales_target=0):
        
        super().__init__(username, password, email=email, role="salesperson")
        
        self.sales_target = sales_target
        self.total_sales = 0

    def to_dict(self):
        
        data = super().to_dict()# Add the specific salesperson fields
        data.update({
            "sales_target": self.sales_target,
            "total_sales": self.total_sales
        })
        return data

    def __str__(self):
        return f"Salesperson(username={self.username}, email={self.email})"