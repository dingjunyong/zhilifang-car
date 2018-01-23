Page({
  data: {
    shop_name:'',
    mobile_number:'',
    mobile_code:'',
    password:'',
    isAgree: true
  },
  bindAgreeChange: function (e) {
    this.setData({
      isAgree: !!e.detail.value.length
    });
  },
  register: function () {
    wx.request({
      url: "http://127.0.0.1/",
      data: {
        shop_name: shop_name,
        mobile_number: mobile_number,
        mobile_code: mobile_code,
        password: password,
      },
      method: "POST",
      success: function (res) {

      },
      fail: function (res) {
        console.log('失败');
      }
    })
  },
});