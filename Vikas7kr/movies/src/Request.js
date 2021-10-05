const API_KEY = "a6dca2d7f795aa810e74ea80deec68fc";

const requests = {
    fetchTrending: `/trending/all/week?api_key=${API_KEY}&language-US`,
    fetchTopRated: `/movie/top_rated?api_key=${API_KEY}&language=en-US`,
    fetchUpcoming:`/movie/upcoming?api_key=${API_KEY}&language=en-US`,
    fetchNetflixOriginals: `/discover/tv?api_key=${API_KEY}&with_networks=213`,
    fetchActionMovies: `/discover/movie?api_key=${API_KEY}&with_genres=28`,
    fetchComedyMovies: `/discover/movie?api_key=${API_KEY}&with_genres=35`,
    fetchHorrorMovies: `/discover/movie?api_key=${API_KEY}&with_genres=27`,
    fetchRomanceMovies: `/discover/movie?api_key=${API_KEY}&with_genres=10749`,
    fetchDocumentariesMovies: `/discover/movie?api_key=${API_KEY}&with_genres=99`,
    fetchTvproviders: `/discover/tv?api_key=${API_KEY}&sort_by=popularity.desc&page=1&timezone=America%2FNew_York&include_null_first_air_dates=true&with_watch_monetization_types=flatrate`,
    fetchDiscoverMovie: `/discover/movie?api_key=${API_KEY}&language=en-US&sort_by=popularity.desc`,
    fetchsearchMovies:`/search/movie?api_key=${API_KEY}&language=en-US&page=1&include_adult=false`,
}

export default requests; 