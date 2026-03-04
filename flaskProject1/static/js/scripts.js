document.addEventListener('DOMContentLoaded', function() {
    // 获取 Flash 消息的容器
    var flashMessages = document.getElementById('flash-messages');

    // 检查 Flash 消息是否存在
    if (flashMessages) {
        // 设置一个 3 秒后执行的定时器
        setTimeout(function() {
            // 隐藏 Flash 消息
            flashMessages.style.display = 'none';
        }, 3000); // 3000 毫秒 = 3 秒
    }
});