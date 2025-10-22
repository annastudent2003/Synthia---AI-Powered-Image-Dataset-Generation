import express from "express";
import { spawn } from "child_process";
import path from "path";
import fs from "fs";
import archiver from "archiver"; 
const router = express.Router();

function zipDirectory(sourceDir, outPath) {
  return new Promise((resolve, reject) => {
    const output = fs.createWriteStream(outPath);
    const archive = archiver("zip", { zlib: { level: 9 } });

    output.on("close", () => resolve());
    archive.on("error", (err) => reject(err));

    archive.pipe(output);
    archive.directory(sourceDir, false);
    archive.finalize();
  });
}

router.post("/", async (req, res) => {
  try {
    const { prompt } = req.body;
    if (!prompt) return res.status(400).json({ error: "Prompt is required" });

    const pythonScript = path.join(process.cwd(), "backend", "python_ml", "annotate_pipeline.py");
    const outputDir = path.join(process.cwd(), "backend", "generated");
    const datasetFolder = path.join(outputDir, "dataset_output");
    const zipPath = path.join(outputDir, "dataset.zip");

    if (!fs.existsSync(outputDir)) fs.mkdirSync(outputDir, { recursive: true });
    if (!fs.existsSync(datasetFolder)) fs.mkdirSync(datasetFolder, { recursive: true });

    console.log(`🧠 Running Python ML pipeline for: "${prompt}"`);

    const pythonProcess = spawn("python", [pythonScript, prompt, datasetFolder]);

    let pythonLogs = "";
    let pythonErrors = "";

    pythonProcess.stdout.on("data", (data) => {
      const msg = data.toString();
      pythonLogs += msg;
      console.log(`PYTHON: ${msg}`);
    });

    pythonProcess.stderr.on("data", (data) => {
      const err = data.toString();
      pythonErrors += err;
      console.error(`PYTHON ERROR: ${err}`);
    });

    pythonProcess.on("close", async (code) => {
      console.log(`🐍 Python exited with code ${code}`);

      if (code !== 0) {
        return res.status(500).json({ error: "Python script failed", details: pythonErrors });
      }

      console.log("📦 Zipping generated dataset...");
      await zipDirectory(datasetFolder, zipPath);
      console.log(`✅ Dataset zipped at: ${zipPath}`);

     const imagePreviews = Array.from({ length: 10 }, (_, i) => ({
        url: `https://picsum.photos/400?random=${Math.floor(Math.random() * 9999)}`,
      }));

      // Send response
      res.json({
        message: "Dataset generated successfully",
        images: imagePreviews,
        datasetZip: "/downloads/dataset.zip",
      });
    });
  } catch (err) {
    console.error("❌ Backend Error:", err);
    res.status(500).json({ error: "Internal Server Error" });
  }
});

export default router;
