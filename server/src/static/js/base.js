$(document).ready(function () {
    $(".clickable-row").click(function () {
        window.location = $(this).data("href");
    });
    $('.select-all').change(function (e) {
        e.preventDefault();
        $('.checkbox-item').prop('checked', $(this).prop("checked"));
    });
    $(".back").click(() => {
        window.history.back();
    })
});

function getCookie(cname) {
    let name = cname + "=";
    let decodedCookie = decodeURIComponent(document.cookie);
    let ca = decodedCookie.split(';');
    for (let i = 0; i < ca.length; i++) {
        let c = ca[i];
        while (c.charAt(0) == ' ') {
            c = c.substring(1);
        }
        if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
        }
    }
    return "";
}

const renderHtml = (url, target = undefined, append = false, prepend = false, data = {}) => {
    $.ajax({
        type: 'POST',
        url: url,
        data: { ...data, csrfmiddlewaretoken: getCookie("csrftoken") },
        success: function (html_res) {
            if (append && target)
                $(target).append(html_res)
            if (prepend && target)
                $(target).prepend(html_res)
        },
        error: function (response) {
            console.log(response)
        }
    })
    return false
}

const request = async (url, method = 'GET', data = {}) => {
    const response = await fetch(url, {
        method: method, // *GET, POST, PUT, DELETE, etc.
        mode: 'cors', // no-cors, *cors, same-origin
        cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
        credentials: 'same-origin', // include, *same-origin, omit
        headers: {
            'Content-Type': 'application/json',
            // 'Content-Type': 'application/x-www-form-urlencoded',
            "X-CSRFToken": getCookie("csrftoken"),
        },
        redirect: 'follow', // manual, *follow, error
        referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
        body: JSON.stringify(data) // body data type must match "Content-Type" header
    });
    if (response.status === 404) {
        throw Error(response.statusText);
    }

    return response.json();
}

const _delete = async (url, reload) => {
    if (confirm('Are you sure you want to Delete?')) {
        await request(url, 'DELETE')
        if (reload) window.location.reload()
    }
}

const _get = async (url) => {
    const res = await request(url)
    return res
}

const _post = async (url, data) => {
    const res = await request(url, 'POST', data)
    return res
}

const _put = async (url, data) => {
    const res = await request(url, 'PUT', data)
    return res
}