# 电影网站

这是一个使用 Django 框架开发的电影网站，允许用户注册、登录并浏览按地区分类的电影。电影分为日韩电影、欧美电影和中国电影。

## 功能

- 用户注册和登录
- 管理员可以通过管理后台管理电影数据
- 按地区分类浏览电影
- 用户必须登录才能访问主页和浏览电影

## 安装步骤
0. **下载项目**

    ```bash
    git clone https://github.com/Ethan-awe/MovieSite.git
    ```
    
1. **安装第三方库**

    ```bash
    pip install -r requirements.txt
    ```

2. **注册管理员（可选）**

    注：已经内置创建了一个管理员，用户名为 `superuser_test`，密码为 `superusertestpass123`。

    ```bash
    python manage.py createsuperuser
    ```

3. **注册用户（可选）**

    注：已经内置创建了一个用户，用户名为 `admin_test`，密码为 `testpassword123`。

4. **运行服务器**

    ```bash
    python manage.py runserver
    ```

5. **访问网站**

    ![image](https://github.com/Ethan-awe/MovieSite/assets/140080063/6117d689-7cb9-4fbb-9c75-e4e0efb6634d)

    Enjoy yourself!

6. **修改信息（增删用户/电影）**
   
    登录管理员账号
   ![image](https://github.com/Ethan-awe/MovieSite/assets/140080063/8cc8ac3c-ea8c-49e6-a391-08b22b52e73f)
   进入“管理后台”界面
   ![image](https://github.com/Ethan-awe/MovieSite/assets/140080063/b0837b64-d72a-43f3-b8a9-bff69d566033)

