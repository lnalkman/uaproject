var popupButton = document.querySelector('.banner button');
var popupMenu = document.getElementsByClassName('popup')[0];
var closePopup = document.getElementById('closer');

popupButton.onclick = function() {
  popupMenu.style.opacity = 1;
  popupMenu.style.zIndex = 1;
}

closePopup.onclick = function() {
  popupMenu.style.opacity = -1;
  popupMenu.style.zIndex = -1;
}
