function ShowImage(id_img) {
    // remove class visibility of current img
    document.getElementsByClassName("gallery_show_big_img")[0].classList.remove("gallery_show_big_img");
    document.getElementsByClassName("gallery_show_little_img")[0].classList.remove("gallery_show_little_img");

    // add visibility classes
    var little_image = document.getElementById("little_image" + id_img);
    var big_image = document.getElementById("big_image" + id_img);
    little_image.classList.add("gallery_show_little_img");
    big_image.classList.add("gallery_show_big_img");

    // set the slider at the good place
    document.getElementsByClassName("slider")[0].style.transform = "translateY(" + ((parseInt(id_img) - 1) * 100) + "%)";

    // show image by sliding
    var images_in_gallery = document.querySelectorAll('.wrap figure')
    for (let i = 0; i < images_in_gallery.length; i++) {
        images_in_gallery[i].style.transform = "translateX(-" + ((parseInt(id_img) - 1) * 100) + "%)";
    }
}