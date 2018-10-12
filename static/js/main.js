let postPreviewBlock = $('#postPreview');
let mainWidth = $('main').width();
let containerWidth = $('.container').outerWidth();
let mainPaddingRight = (mainWidth - containerWidth) / 2;
let postPreviewWidth = $('#sidebar').outerWidth() + mainPaddingRight;

postPreviewBlock.css({
    'right': '-' + postPreviewWidth + 'px'
});

// Open post preview
$("[data-target=post-preview]").click(function (e) {
  e.preventDefault();
  $.get($(e.target).attr('href'), function (html) {
      postPreviewBlock.html(html);
  });

  postPreviewBlock.css({
    'width': postPreviewWidth + 'px',
    'right': 0,
    'position': 'fixed'
  });
});

// Close post preview
$('body').on('click', '#postPreviewClose', function () {
  postPreviewBlock.css({
    'right': '-' + postPreviewWidth + 'px'
  });

  setTimeout(function() {
      $('#postPreview').html('');
  }, 700);
});