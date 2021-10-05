import React from 'react';
import './App.css';
import Row from "./Row.js"
import requests from './Request.js';
import Nav from './Nav.js';
  
function App() {
  return (
    <div className="app">
      <Nav />
      <Row title="Trending Now" fetchUrl={requests.fetchTrending}
      isLargeRow
      />
      <Row title="Top rated" fetchUrl={requests.fetchTopRated} isLargeRow />
      <Row title="Upcoming movies" fetchUrl={requests.fetchUpcoming} isLargeRow/>
      <Row title="Netflix Originals" fetchUrl={requests.fetchNetflixOriginals} isLargeRow />
      <Row title="Action movies" fetchUrl={requests.fetchActionMovies} isLargeRow/>
      <Row title="Comedy movies" fetchUrl={requests.fetchComedyMovies} isLargeRow/>
      <Row title="Romance movies" fetchUrl={requests.fetchRomanceMovies} isLargeRow/>
      <Row title="Horror movies" fetchUrl={requests.fetchHorrorMovies} isLargeRow />
      <Row title="Movie providers" fetchUrl={requests.fetchDiscoverMovie} isLargeRow />
      <Row title="Tv providers" fetchUrl={requests.fetchTvproviders} isLargeRow/>
      <Row title="Documentaries" fetchUrl={requests.fetchDocumentariesMovies} isLargeRow/>
    </div>
  );
}

export default App;
