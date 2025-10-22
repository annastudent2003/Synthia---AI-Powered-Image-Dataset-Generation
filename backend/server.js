import express from "express";
import cors from "cors";
import path from "path";
import generateRoute from "./routes/generate.js";

const app = express();
app.use(
  cors({
    origin: ["http://localhost:3000"],
    methods: ["GET", "POST"],
  })
);

app.use(express.json());

app.use("/downloads", express.static(path.join(process.cwd(), "backend", "generated")));

app.use("/generate", generateRoute);

app.get("/", (req, res) => res.send("Backend running locally and connected to Python ML"));

const PORT = 5000;
app.listen(PORT, "0.0.0.0", () => console.log(`Backend running on port ${PORT}`));
