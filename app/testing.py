from models import Product
from api.services import get_products
from flask_login import current_user

x = get_products(12)
print(f"~~~~{x}")

p = Product(title=x['product_name'],price=x['price'],description=x['description'],category=x['category'],img_url=x['product_image'])

p.saveProduct()

# TO add to DB
@app.route('/sendit')
def sendIt():
    x = get_products(20)
    print("ADDED TO DB")
    p = Product(product_id=x['product_id'],title=x['product_name'],price=x['price'],description=x['description'],category=x['category'],img_url=x['product_image'])
    p.saveProduct()
    return render_template('index.html')

#html for it
        # <a class="btn btn-outline-dark justify-content-end" href="{{ url_for('sendIt') }}"
        # role="button">DONT PRESS THIS BUTTON. ITS A FUNCITON TO ADD ITEMS TO DB</a>


#delete from db
 