function like(postId) {
    // Get the elements for displaying the like count and the like button
    const likeCount = document.getElementById(`likes-count-${postId}`);
    const likeButton = document.getElementById(`like-button-${postId}`);
  
    // Send a POST request to the "/like-post/<post_id>" endpoint to like or unlike the post
    fetch(`/like-post/${postId}`, { method: "POST" })
      .then((res) => res.json())
      .then((data) => {
        // Update the like count with the data received from the server
        likeCount.innerHTML = data["likes"];
        // Change the appearance of the like button based on whether the user liked the post or not
        if (data["liked"] === true) {
          likeButton.className = "fas fa-thumbs-up";
        } else {
          likeButton.className = "far fa-thumbs-up";
        }
      })
      .catch((e) => alert("Could not like post.")); // Handle errors if the request fails
  }