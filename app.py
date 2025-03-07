from flask import Flask, render_template, request, redirect, url_for, flash, session
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Bộ nhớ tạm để demo (nên thay bằng database trong dự án thực tế)
users = {
    'admin': {'password': 'admin', 'blocked': False}  # Tạo tài khoản admin mặc định
}

from datetime import datetime

posts = [
    {'id': 1, 'content': 'Cuộc sống không phải lúc nào cũng dễ dàng, nhưng điều quan trọng là chúng ta luôn phải nhìn về phía trước.', 'username': 'NguyenThiLan', 'timestamp': datetime.now()},
    {'id': 2, 'content': 'Sự kiên trì chính là chìa khóa để vượt qua mọi khó khăn trong cuộc sống. Hãy luôn cố gắng, dù đôi khi thất bại.', 'username': 'TranThiKim', 'timestamp': datetime.now()},
    {'id': 3, 'content': 'Trong công việc, việc quản lý thời gian là rất quan trọng. Hãy học cách sắp xếp công việc một cách hợp lý.', 'username': 'LeAnhTuan', 'timestamp': datetime.now()},
    {'id': 4, 'content': 'Đôi khi những thất bại lớn lại là bài học quý giá giúp chúng ta trưởng thành hơn rất nhiều.', 'username': 'PhamMinhTuan', 'timestamp': datetime.now()},
    {'id': 5, 'content': 'Mỗi ngày trôi qua là một cơ hội mới để chúng ta thay đổi và cải thiện bản thân.', 'username': 'NguyenQuyen', 'timestamp': datetime.now()},
    {'id': 6, 'content': 'Hãy luôn sống với đam mê và niềm tin vào bản thân, vì đó chính là điều khiến bạn khác biệt trong cuộc sống này.', 'username': 'HoangThanhHien', 'timestamp': datetime.now()},
    {'id': 7, 'content': 'Đôi khi chúng ta cần một chút thời gian yên tĩnh để nhìn lại bản thân và hiểu được những gì thực sự quan trọng.', 'username': 'VuThiLan', 'timestamp': datetime.now()},
    {'id': 8, 'content': 'Mọi người thường hay nói về hạnh phúc, nhưng thực sự thì nó đến từ sự hài lòng với chính bản thân mình.', 'username': 'NguyenHongAnh', 'timestamp': datetime.now()},
    {'id': 9, 'content': 'Cuộc sống không phải lúc nào cũng theo kế hoạch, nhưng chúng ta luôn có thể chọn cách đối mặt với thử thách.', 'username': 'LeThiNgoc', 'timestamp': datetime.now()},
    {'id': 10, 'content': 'Đôi khi, sự thấu hiểu và chia sẻ chính là thứ mà mọi người cần nhất trong một cộng đồng.', 'username': 'TruongHongSon', 'timestamp': datetime.now()},
    {'id': 11, 'content': 'Tôi nghĩ rằng mỗi người đều có khả năng làm thay đổi thế giới, bắt đầu từ những điều nhỏ nhất trong cuộc sống.', 'username': 'PhanQuocDuy', 'timestamp': datetime.now()},
    {'id': 12, 'content': 'Chúng ta không thể kiểm soát mọi thứ, nhưng có thể điều chỉnh cách nhìn nhận và phản ứng với những tình huống đó.', 'username': 'NguyenThuTrang', 'timestamp': datetime.now()},
    {'id': 13, 'content': 'Sự tử tế không chỉ thay đổi người khác mà còn thay đổi chính bản thân mình. Hãy luôn sống với một trái tim nhân hậu.', 'username': 'PhanTienDuy', 'timestamp': datetime.now()},
    {'id': 14, 'content': 'Cuộc sống này ngắn ngủi, vì vậy đừng lãng phí thời gian vào những điều không đáng, hãy sống hết mình!', 'username': 'TranThiBao', 'timestamp': datetime.now()},
    {'id': 15, 'content': 'Chúng ta cần học cách đối mặt với nỗi sợ hãi của chính mình, đó là cách duy nhất để chúng ta vượt qua nó.', 'username': 'LeMinhKhoa', 'timestamp': datetime.now()},
    {'id': 16, 'content': 'Mỗi người đều có những thử thách riêng trong cuộc sống, nhưng cách chúng ta vượt qua chúng mới là điều quan trọng.', 'username': 'NguyenBichThao', 'timestamp': datetime.now()},
    {'id': 17, 'content': 'Đừng để nỗi sợ làm chậm lại bước tiến của bạn, hãy dũng cảm bước đi và đối mặt với mọi thử thách.', 'username': 'HoangBichThao', 'timestamp': datetime.now()},
    {'id': 18, 'content': 'Mỗi ngày trôi qua là một cơ hội mới, đừng để những khó khăn cản bước bạn. Hãy luôn tiến lên.', 'username': 'TrinhThao', 'timestamp': datetime.now()},
    {'id': 19, 'content': 'Tôi học được rằng đôi khi, sự im lặng chính là câu trả lời tốt nhất cho những điều không đáng phải tranh cãi.', 'username': 'VuMinhTam', 'timestamp': datetime.now()},
    {'id': 20, 'content': 'Sự hạnh phúc không phải là một đích đến, mà là hành trình bạn đi qua mỗi ngày với những quyết định tốt đẹp.', 'username': 'NguyenThanhTuan', 'timestamp': datetime.now()},
    {'id': 21, 'content': 'Để tạo ra một cộng đồng thật sự mạnh mẽ, mỗi người cần phải biết chia sẻ và lắng nghe những người xung quanh.', 'username': 'TrieuQuyen', 'timestamp': datetime.now()},
    {'id': 22, 'content': 'Dù cuộc sống có khó khăn đến đâu, hãy luôn tin vào khả năng của bản thân và không bao giờ bỏ cuộc.', 'username': 'LeThiThuy', 'timestamp': datetime.now()},
    {'id': 23, 'content': 'Mỗi người đều có một ước mơ riêng, hãy theo đuổi ước mơ đó với tất cả đam mê và quyết tâm.', 'username': 'NguyenThanhSon', 'timestamp': datetime.now()},
    {'id': 24, 'content': 'Chúng ta không thể thay đổi quá khứ, nhưng chúng ta có thể làm cho hiện tại trở nên tốt đẹp hơn.', 'username': 'PhamThiNguyen', 'timestamp': datetime.now()},
    {'id': 25, 'content': 'Cuộc sống này luôn có những cơ hội mới, điều quan trọng là bạn có đủ dũng cảm để nắm bắt chúng hay không.', 'username': 'TranMaiTam', 'timestamp': datetime.now()},
]


# Trang chủ hiển thị danh sách bài viết với phân trang
@app.route('/')
def home():
    # Mặc định mỗi trang chỉ hiển thị 10 bài viết
    posts_per_page = 10
    page = request.args.get('page', 1, type=int)

    # Lấy các bài viết theo trang
    start = (page - 1) * posts_per_page
    end = start + posts_per_page
    paginated_posts = posts[start:end]

    # Tính toán tổng số trang
    total_posts = len(posts)
    total_pages = (total_posts + posts_per_page - 1) // posts_per_page

    return render_template('home.html', posts=paginated_posts, page=page, total_pages=total_pages)

# Các route và chức năng khác không thay đổi

# Trang đăng ký
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if username in users:
            flash("Người dùng đã tồn tại", 'error')
        else:
            users[username] = {'password': password, 'blocked': False}
            flash("Đăng ký thành công, mời đăng nhập", 'success')  # Thêm thông báo flash
            return redirect(url_for('login'))  # Chuyển hướng đến trang đăng nhập sau khi đăng ký thành công
    
    return render_template('register.html')

# Trang đăng nhập
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = users.get(username)
        if user:
            if user['blocked']:
                flash("Tài khoản của bạn đã bị khóa", 'error')
                return redirect(url_for('login'))

            if user.get('password') == password:
                session['username'] = username  # Thiết lập session đúng
                flash("Đăng nhập thành công", 'success')

                # Nếu là admin, chuyển tới trang quản trị
                if username == 'admin':
                    return redirect(url_for('admin'))

                return redirect(url_for('home'))  # Chuyển hướng về trang chủ sau khi đăng nhập thành công
            else:
                flash("Sai thông tin đăng nhập", 'error')
        else:
            flash("Sai thông tin đăng nhập", 'error')

    return render_template('login.html')


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    # Kiểm tra nếu người dùng chưa đăng nhập hoặc không phải là admin
    if 'username' not in session or session['username'] != 'admin':
        flash("Bạn không có quyền truy cập vào trang admin", 'error')
        return redirect(url_for('home'))  # Chuyển về trang chủ nếu không phải admin

    if request.method == 'POST':
        action = request.form.get('action')
        username = request.form.get('username')

        if username == 'admin':
            flash("Không thể thay đổi tài khoản admin", 'error')  # Không thay đổi tài khoản admin
        elif username in users:
            if action == 'block':
                users[username]['blocked'] = True
                flash(f"Đã khóa tài khoản của {username}", 'success')  # Thông báo khóa tài khoản thành công
            elif action == 'reset':
                users[username]['password'] = 'defaultpassword'
                flash(f"Đã reset mật khẩu cho {username}", 'success')  # Thông báo reset mật khẩu thành công
            elif action == 'unblock':
                users[username]['blocked'] = False
                flash(f"Đã mở khóa tài khoản của {username}", 'success')  # Thông báo mở khóa tài khoản thành công

    return render_template('admin.html', users=users)

# Trang tạo bài viết mới
@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if 'username' not in session:
        flash("Bạn cần đăng nhập để tạo bài viết", 'error')
        return redirect(url_for('login'))

    if request.method == 'POST':
        content = request.form.get('content')
        if content:
            new_post = {
                'id': len(posts) + 1, 
                'content': content,
                'username': session['username'],  # Lưu tên người dùng từ session
                'timestamp': datetime.now()
            }
            posts.append(new_post)
            flash("Bài viết đã được tạo thành công", 'success')
            return redirect(url_for('home'))
        else:
            flash("Nội dung bài viết không được để trống", 'error')

    return render_template('create_post.html')
#Quản lý posts
@app.route('/manage_posts', methods=['GET', 'POST'])
def manage_posts():
    if 'username' not in session:
        flash("Bạn cần đăng nhập để thực hiện thao tác này", 'error')
        return redirect(url_for('login'))

    # Lọc các bài viết của người dùng hiện tại
    user_posts = [post for post in posts if post['username'] == session['username']]

    if request.method == 'POST':
        post_ids_to_delete = request.form.getlist('post_ids')
        if not post_ids_to_delete:
            flash("Bạn chưa chọn bài viết nào để xóa", 'error')
            return redirect(url_for('manage_posts'))

        # Xóa bài viết đã chọn
        global postsS
        postsS = [post for post in posts if post['id'] not in map(int, post_ids_to_delete)]

        flash("Bài viết đã được xóa thành công", 'success')
        return redirect(url_for('home'))

    return render_template('manage_posts.html', posts=user_posts)


# Trang đăng xuất
@app.route('/logout')
def logout():
    session.pop('username', None)  # Xóa session người dùng
    flash("Bạn đã đăng xuất", 'success')
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
