<template>
  <div>
    <div class="columns">
      <div ref="main" id="hi" class="column is-three-quarters">
        <div class="heading pb-6 mb-6">
          <span class="pl-3 is-size-1 myTitle"
            ><span class="has-text-grey ">Watch</span>Weather</span
          >
        </div>
        <div class="bottom pt-6 mt-6">
          <div class="showBar">
            <p class="temp">{{ temp.toFixed(0) }}°C</p>
            <div class="qoutes ml-6">
              <p class="quote">"{{ quote }}"</p>
              <span class="author pl-3">~ {{ author }}</span>
            </div>
          </div>
          <div class="date mt-6 pt-6">
            <p class="mr-6 detail">
              <span class="has-text-weight-semibold"> DATE</span>{{ date }}
            </p>
            <p class="mr-6 detail">
              <span class="has-text-weight-semibold">TIME</span>{{ time }}
            </p>
            <p class="mr-6 detail">
              <span class="has-text-weight-semibold"> FEELS LIKE</span
              >{{ feelsLike }}°C
            </p>
            <p class="mr-6 detail">
              <span class="has-text-weight-semibold"> MIN TEMP</span
              >{{ minTemperature }}°C
            </p>
            <p class="mr-6 detail">
              <span class="has-text-weight-semibold">MAX TEMP</span>
              {{ maxTemperature }}°C
            </p>
            <p class="mr-6 detail">
              <span class="has-text-weight-semibold"> WEATHER</span
              >{{ weather }}
            </p>
          </div>
        </div>
        <hr />
        <div class="imgChange">
          <button
            class="button is-primary is-inverted is-outlined"
            @click="changeImg"
          >
            Change Image
          </button>
        </div>
      </div>
      <div class="column is-one-quarters">
        <div class="outermost mt-2 ">
          <p class="outside mb-2">{{ location }}</p>
          <p class="inside">
            <span class="inside2">Latitude:</span>
            <span class="inside3">{{ lat.toFixed(4) }}</span>
            <span class="inside2">Longitude:</span>
            <span class="inside3">{{ lon.toFixed(4) }}</span>
          </p>
          <p class="inside"></p>
        </div>
        <hr />
        <div class="outermost mt-6 ">
          <p class="outside2 mb-2">Weather Details</p>
          <p class="inside">
            <span class="inside2"> Wind:</span>
            <span class="inside3">{{ wind }}Kmph</span>
          </p>
          <p class="inside">
            <span class="inside2"> Humidity:</span
            ><span class="inside3">{{ humidity }}%</span>
          </p>
          <p class="inside">
            <span class="inside2"> Pressure:</span
            ><span class="inside3">{{ pressure }}hPa</span>
          </p>
          <p class="inside">
            <span class="inside2"> Clouds:</span
            ><span class="inside3">{{ clouds }}%</span>
          </p>
          <p class="inside">
            <span class="inside2">Description:</span
            ><span class="inside3">{{ description }}</span>
          </p>
        </div>
        <hr />
        <div class="outermost mt-6 ">
          <p class="outside2 mb-2">Sunrise & Sunset</p>
          <p class="inside">
            <span class="inside2"> Sunrise:</span>
            <span class="inside3">{{ sunrise }}</span>
          </p>
          <p class="inside">
            <span class="inside2"> Sunset:</span
            ><span class="inside3">{{ sunset }}</span>
          </p>
        </div>
      </div>
    </div>
    <footer class="footer pt-0 pb-3">
      <div class="content has-text-centered">
        <p>
          <strong>Made By Apala Singh </strong>~
          <a href="https://github.com/ApalaS/watch-weather"> Leave a ❤️ </a>~
          <a href="https://www.linkedin.com/in/apala-singh-a23818202/">
            Linkedin </a
          >~
          <a href="https://www.linkedin.com/in/apala-singh-a23818202/">
            Github </a
          >~ <strong> mail at: </strong
          ><a href="mailto:apalasingh2001@gmail.com">apalasingh2001@gmail.com</a
          >.
        </p>
      </div>
    </footer>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      quote: null,
      image: null,
      forecast: null,
      lat: null,
      lon: null,
      alert: null,
      sunrise: null,
      sunset: null,
      temp: null,
      feelsLike: null,
      time: null,
      wind: null,
      humidity: null,
      pressure: null,
      clouds: null,
      weather: null,
      description: null,
      date: null,
      author: null,
      minTemperature: null,
      maxTemperature: null,
      location: null,
    };
  },
  beforeMount() {
    navigator.geolocation.getCurrentPosition((position) => {
      this.lat = position.coords.latitude;
      this.lon = position.coords.longitude;
      console.log(this.lat, this.lon);

      axios.get("https://api.quotable.io/random").then((response) => {
        this.quote = response.data.content;
        this.author = response.data.author;
      });

      axios
        .get(
          `https://api.openweathermap.org/data/2.5/onecall?lat=${this.lat}&lon=${this.lon}&units=metric&appid=006de37c33466228906e42303c5cf9da`
        )
        .then((response) => {
          console.log(response);
          this.alert = response.data.alerts?.event;
          this.sunrise = response.data.current.sunrise;
          this.sunset = response.data.current.sunset;
          this.temp = response.data.current.temp;
          this.feelsLike = response.data.current.feels_like;
          this.wind = response.data.current.wind_speed;
          this.humidity = response.data.current.humidity;
          this.pressure = response.data.current.pressure;
          this.clouds = response.data.current.clouds;
          this.weather = response.data.current.weather[0].main;
          this.description = response.data.current.weather[0].description;
          this.minTemperature = response.data.daily[0].temp.min;
          this.maxTemperature = response.data.daily[0].temp.max;
          // console.log(this.alert);
          axios
            .get(
              `https://api.unsplash.com/photos/random?client_id=4j3NCVWHWBF6uM9LlfrF_NQvO8J5AFOpvHd9lT6ZnzI&query=${this.weather}-dark`
            )
            .then((response) => {
              this.image = response.data.urls.regular;
              this.$refs["main"].style.background = `url(${this.image})`;
              this.$refs["main"].style.backgroundSize = "cover";
              this.$refs["main"].style.backgroundRepeat = "no-repeat";
              //console.log(response.data);
            });
          let x = new Date();
          this.time =
            x.getHours() +
            ":" +
            (x.getMinutes() < 10 ? `0${x.getMinutes()}` : x.getMinutes());
          this.date = x.getDate() + "/" + x.getMonth() + "/" + x.getYear();
        });

      axios
        .get(
          `https://api.openweathermap.org/data/2.5/weather?lat=${this.lat}&lon=${this.lon}&units=metric&appid=006de37c33466228906e42303c5cf9da`
        )
        .then((response) => {
          console.log(response.data);
          this.location = response.data.name;
        });
    });
  },

  methods: {
    changeImg() {
      axios
        .get(
          `https://api.unsplash.com/photos/random?client_id=4j3NCVWHWBF6uM9LlfrF_NQvO8J5AFOpvHd9lT6ZnzI&query=${this.weather}-dark`
        )
        .then((response) => {
          this.image = response.data.urls.regular;
          this.$refs["main"].style.background = `url(${this.image})`;
          this.$refs["main"].style.backgroundSize = "cover";
          this.$refs["main"].style.backgroundRepeat = "no-repeat";
          //console.log(response.data);
        });
    },
  },
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css2?family=PT+Sans:ital,wght@0,400;0,700;1,400;1,700&display=swap");
@import url("https://fonts.googleapis.com/css2?family=Bebas+Neue&display=swap");

.myTitle {
  font-family: "Bebas Neue", cursive;
  color: #fff;
  font-size: 2rem;
  font-weight: 700;
}
.heading {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  padding: 2rem;
}

.showBar {
  display: flex;
  flex-direction: row;
  justify-content: flex-start;
  align-content: flex-end;
}
.temp {
  font-size: 12rem;
  font-weight: 700;
  line-height: 0.7;
  /* font-family: "PT Sans", sans-serif; */
}
.columns {
  display: flex;
  height: 100vh;
  width: 100%;
  font-family: "PT Sans", sans-serif;
}
.bottom {
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  align-items: flex-start;
  width: 100%;
  padding: 2rem;
  color: rgba(255, 255, 255, 0.9);
  font-family: "PT Sans", sans-serif;
}
.quote {
  font-size: 1.25rem;
  text-transform: capitalize;
  margin: 1rem;
  font-weight: 700;
  width: 90%;
}
.quotes {
  display: flex;
  flex-direction: column;
}
.date {
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
.detail {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}
.outside {
  font-size: 1.5em;
  font-weight: 700;
  padding-top: 3 rem;
  padding-bottom: 3 rem;
  margin-top: 6 rem;
  margin-bottom: 6 rem;
}
.outside2 {
  font-size: 1em;
  font-weight: 700;
  margin-top: 1em;
  margin-bottom: 1em;
  letter-spacing: 0.05em;
}
.inside {
  font-size: 1em;
  font-weight: 400;
  color: #7f7f7f;
}
.outermost {
  display: flex;
  flex-direction: column;
}
.inside3 {
  color: #000000;
  font-weight: 700;
}
.inside {
  padding-left: 1em;
  padding-right: 1em;
  display: flex;
  justify-content: space-between;
}
hr {
  border-top: 1px solid rgba(127, 127, 127, 0.5);
  border-bottom: 1px solid rgba(127, 127, 127, 0.5);
  border-radius: 100%;
  margin-left: 0.5em;
  margin-top: 2em;
  margin-bottom: 2em;
}
.imgChange {
  display: flex;
  justify-content: flex-end;
  margin-right: 2 em;
}
</style>
