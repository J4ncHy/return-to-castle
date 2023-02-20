import express, { Express, Request, Response } from "express";
import { Schema, model, connect, connection } from "mongoose";
import bodyParser from "body-parser";

const app: Express = express();
const port: number = 3000;

app.use(bodyParser.json());

connect(`mongodb://192.168.128.8:32768/RTC_score`);
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
        let insert = new mod({ player: req.body.player, level: req.body.level, score: req.body.score, time: req.body.time });
        await insert.save();
    } catch (error) {
        console.log(error);
        res.status(400).send("Bad data");
    }

    res.send("Add successful");
});

app.get("/api/read", (req: Request, res: Response) => {
    res.send("read");
});

app.get("/api/read-best", (req: Request, res: Response) => {
    res.send("read-best");
});

app.put("/api/update", (req: Request, res: Response) => {
    res.send("create test");
});

app.delete("/api/delete", (req: Request, res: Response) => {
    res.send("create test");
});

app.listen(port, () => console.log(`Example app listening on port ${port}!`));
