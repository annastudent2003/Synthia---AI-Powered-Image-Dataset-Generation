import { useState } from "react";
import { useNavigate } from "react-router-dom";
import bgVideo from "../assets/bg-video.mp4";
import "./Home.css";
<style>
@import url('https://fonts.googleapis.com/css2?family=Barriecito&family=DM+Serif+Display&family=Lato:wght@700&family=Lavishly+Yours&family=Merriweather:ital,opsz,wght@0,18..144,300..900;1,18..144,300..900&family=Montserrat:ital,wght@0,100..900;1,100..900&family=Noto+Sans:ital,wght@0,100..900;1,100..900&family=Play&family=Roboto+Mono:ital,wght@0,100..700;1,100..700&family=Rock+Salt&family=Shadows+Into+Light&display=swap');
</style>
export default function Home() {
  const [prompt, setPrompt] = useState("");
  const navigate = useNavigate();

  const handleSearch = (e) => {
    e.preventDefault();
    if (prompt.trim() !== "") {
      navigate(`/results?prompt=${encodeURIComponent(prompt)}`);
    }
  };

  return (
    <div className="home-container">
      <video className="background-video" autoPlay loop muted>
        <source src={bgVideo} type="video/mp4" />
      </video>
      <div className="overlay">
        <div className="content-box">
          <h1>Synthia</h1>
          <p>
            Turn your ideas into
            <br />
           ready to use AI training data in seconds.
          </p>
          <form onSubmit={handleSearch} className="search-bar">
            <input
              type="text"
              placeholder="Type your prompt..."
              value={prompt}
              onChange={(e) => setPrompt(e.target.value)}
            />
            <button type="submit">Search</button>
          </form>
        </div>
      </div>
    </div>
  );
}
