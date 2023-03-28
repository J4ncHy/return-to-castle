import express, { Express, Request, Response } from "express";
import { Schema, model, connect, connection } from "mongoose";
import bodyParser from "body-parser";

const app: Express = express();
const port: number = 3000;

app.use(bodyParser.json());

app.use((req, res, next) => {
    res.append('Access-Control-Allow-Origin', ['*']);
    res.append('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE');
    res.append('Access-Control-Allow-Headers', 'Content-Type');
    next();
});

connect(`mongodb://192.168.128.8:27017/RTC_score`);
const db = connection;

db.on("error", console.error.bind(console, "connection error: "));
db.once("open", () => {
    console.log("Connected successfully");
});

const schema: Schema = new Schema({
    player: { type: String, required: true },
    level: { type: Number, required: true },
    score: { type: Number, required: true },
    time: { type: Number, required: true },
});

const mod = model("scoreboards", schema);

app.put("/api/create", async (req: Request, res: Response) => {
    try {
        //console.log(req.body);
        let max_score: { [id: number]: number } = { 0: 50, 1: 150, 2: 250, 3: 350 };

        if (req.body.score > max_score[req.body.level] || req.body.score < 0) throw new Error("Incorrect score");

        let insert = new mod({ player: req.body.player, level: req.body.level, score: req.body.score, time: req.body.time });
        await insert.save();
        res.send("Successfully added");
    } catch (error) {
        console.log(error);
        res.status(400).send("Bad data");
    }
});

app.post("/api/read-per-level", async (req: Request, res: Response): Promise<void> => {
    try {
        const results = await mod.find({ level: req.body.level }).sort({ score: -1, time: 1 }).limit(5).exec();

        res.send(results);
    } catch (error) {
        res.status(500).send(error);
    }
});

/*
app.get("/api/read", (req: Request, res: Response) => {
    res.send("read");
});
*/

/*
app.put("/api/update", (req: Request, res: Response) => {
    res.send("create test");
});

app.delete("/api/delete", (req: Request, res: Response) => {
    res.send("create test");
});
*/

app.listen(port, () => console.log(`Example app listening on port ${port}!`));
