// tạo trình xử lý sự kiện khi ấn nút add vào giỏ hàng (1-21)
var updateBtns = document.getElementsByClassName('update-cart') 

for( i = 0; i< updateBtns.length; i++){
    updateBtns[i].addEventListener('click', function()
    {
        var productId = this.dataset.product
        var action = this.dataset.action
        console.log('productId:' , productId, 'action:', action)

        console.log('USER:', user) 
        if (user == 'AnonymousUser') // kiểm tra trạng thái người dùng đã đăng nhập hay chưa đăng nhập (12-19)
        {
            console.log('Not logged in')
        }
        else
        {
           updateUserOrder(productId,action)
        }
    })
}

function updateUserOrder(productId, action)     // cập nhật đơn đặt hàng của người dùng (API)
{
    console.log("User is logged in")
    var url = '/update_item/'       // url chế độ xem

    fetch(url,{     // lệnh nạp dữ liệu sau mỗi thao tác thêm sản phẩm vào url để cập nhật mặt hàng
        method: 'POST',
        headers:
        {
            'Content-Type' : 'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({'productId': productId, 'action': action})     // các dữ liệu được gửi dưới dạng chuỗi 
        
    })

    .then((response) =>{        // trả lại phản hồi dạng JSON đến view
        return response.json()
    })
    .then((data) =>{       
        
        console.log('data:', data)   // xử lý dữ liệu
        location.reload()
    });
}