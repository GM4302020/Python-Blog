$(document).ready(function(){
    $('#btn-add_review').click(function(e){
        e.preventDefault()

        var user_id = $('#user_id').val()
        var post_id = $('#post_id').val()
        var review = $('#review_id').val()
        var csrftoken = $(this).data('csrftoken')

        console.log(user_id, post_id, review, csrftoken)

        $.ajax({
            url: "/reviewonpost/",
            type: "post",
            headers: {"X-CSRFToken": csrftoken},
            data:{
                user_id : user_id,
                post_id : post_id,
                review: review
            },
            success: function(result){
                location.reload()
            },
            error: function(request, status, error){
                console.log(request, status, error)
            }
        })

    })
})