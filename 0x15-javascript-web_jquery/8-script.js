$.ajax({
    "url":"https://swapi-api.alx-tools.com/api/films/?format=json",
    "success": (data) => {
        if (data){
            for (dicti of data.results){
                $("UL#list_movies").append(`<li>${dicti.title}</li>`)
                //console.log(dicti.title)
            }
        }
    }
})
