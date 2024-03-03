

html方法:  
id跳轉，<a> - href ,
#href :

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Control Page Redirect with ID</title>
  <style>
    body {
      font-family: Arial, sans-serif;
    }
    .container {
      max-width: 600px;
      margin: 0 auto;
      padding: 20px;
    }
    .hidden {
      display: none;
    }
  </style>
</head>
<body>
  <div class="container">
    <div id="page1" class="page">
      <h1>Welcome to Page 1</h1>
      <p>This is Page 1 content.</p>
      <a href="#page2">Go to Page 2</a>
    </div>
    <div id="page2" class="page hidden">
      <h1>Welcome to Page 2</h1>
      <p>This is Page 2 content.</p>
      <a href="#page1">Go to Page 1</a>
      <a href="#page3">Go to Page 3</a>
    </div>
    <div id="page3" class="page hidden">
      <h1>Welcome to Page 3</h1>
      <p>This is Page 3 content.</p>
      <a href="#page1">Go to Page 1</a>
    </div>
  </div>

  <script>
    document.addEventListener('DOMContentLoaded', function() {
      // 获取所有页面元素
      const pages = document.querySelectorAll('.page');

      // 遍历所有页面元素
      pages.forEach(page => {
        // 监听每个页面中的链接点击事件
        page.querySelectorAll('a').forEach(link => {
          link.addEventListener('click', function(event) {
            // 阻止默认链接行为
            event.preventDefault();

            // 获取目标页面的 ID
            const targetId = this.getAttribute('href').substring(1);

            // 隐藏所有页面
            pages.forEach(page => {
              page.classList.add('hidden');
            });

            // 显示目标页面
            document.getElementById(targetId).classList.remove('hidden');
          });
        });
      });
    });
  </script>
</body>
</html>


      <p>Shopping Cart:</p>
      <ul id="cart-items"></ul> <!-- 已加入的商品名称 -->
