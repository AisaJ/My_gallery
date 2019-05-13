$(document).ready(function(){
  
  $('.fancybox').fancybox({
      afterShow: function() {
        this.title = $(this.element).data("caption");
      }
  });

  $('[data-fancybox]').fancybox({
    protect: true,
    closeExisting: false,
    keyboard: true,
    preventCaptionOverlap: true,
    arrows: true,
    loop:true,
    title:{ type:'inside' },
    buttons: [
      "zoom",
      //"share",
      "slideShow",
      "fullScreen",
      "download",
      "thumbs",
      "close"
    ],
    
    animationEffect: "fade",
    selector : '[data-fancybox="gallery"]',
    loop     : true,
    caption : function(instance, item) {
      return this.dataset.caption || '';
    }
  });

  $('.link-class').hide()
});
