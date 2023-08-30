const showMenu = () => {
    const navbar = document.getElementById('navbar-default');
    const navbarItems = document.getElementById('navbar-menu-items');
    let navClasses = navbar.classList;
    let itemClasses = navbarItems.classList;
    navClasses.toggle("bg-[rgba(0,0,0,0.5)]");
    navClasses.toggle("md:bg-transparent");
    itemClasses.toggle("hidden");
}




function clickHandler(e){
    const navbar = document.getElementById('navbar-default');
    const navbarItems = document.getElementById('navbar-menu-items');
    let navClasses = navbar.classList;
    let itemClasses = navbarItems.classList;
    navClasses.toggle("bg-[rgba(0,0,0,0.5)]");
    navClasses.toggle("md:bg-transparent");
    itemClasses.toggle("hidden");
    const href = e.getAttribute("href");
    const offsetTop = document.querySelector(href).offsetTop;
    scroll({
        top: offsetTop,
        behavior: 'smooth'
    });
}
