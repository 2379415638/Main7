function send() {
    var nodemailer = require('nodemailer');
    var smtpTransport = require('nodemailer-smtp-transport');

// 开启一个 SMTP 连接池
    var transport = nodemailer.createTransport(smtpTransport({
        host: "smtp.mxhichina.com", // 主机
        secure: true, // 使用 SSL
        secureConnection: true, // 使用 SSL
        port: 465, // SMTP 端口
        auth: {
            user: "postmaster@seeksrq.top", // 账号
            pass: "lsrq.0218" // 密码
        }
    }));

// 设置邮件内容
    var mailOptions = {
        from: "postmaster@seeksrq.top", // 发件地址
        to: "2379415638@qq.com", // 收件列表
        subject: "Hello world", // 标题
        text:"Hello",
        html:"<p>Hello</p>"
    };

// 发送邮件
    transport.sendMail(mailOptions, function (error, response) {
        if (error) {
            console.error(error);
        } else {
            console.log(response);
        }
        transport.close(); // 如果没用，关闭连接池
    });
}
send();