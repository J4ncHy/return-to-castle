"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express"));
const mongoose_1 = require("mongoose");
const body_parser_1 = __importDefault(require("body-parser"));
const app = (0, express_1.default)();
const port = 3000;
app.use(body_parser_1.default.json());
(0, mongoose_1.connect)(`mongodb://192.168.128.8:32768/RTC_score`);
const db = mongoose_1.connection;
db.on("error", console.error.bind(console, "connection error: "));
db.once("open", () => {
    console.log("Connected successfully");
});
const schema = new mongoose_1.Schema({
    player: { type: String, required: true },
    level: { type: Number, required: true },
    score: { type: Number, required: true },
    time: { type: Number, required: true },
});
const mod = (0, mongoose_1.model)("scoreboards", schema);
app.put("/api/create", (req, res) => __awaiter(void 0, void 0, void 0, function* () {
    try {
        //console.log(req.body);
        let max_score = { 0: 50, 1: 150, 2: 250, 3: 350 };
        if (req.body.score > max_score[req.body.level] || req.body.score < 0)
            throw new Error("Incorrect score");
        let insert = new mod({ player: req.body.player, level: req.body.level, score: req.body.score, time: req.body.time });
        yield insert.save();
    }
    catch (error) {
        console.log(error);
        res.status(400).send("Bad data");
    }
    res.send("Successfully added");
}));
app.post("/api/read-per-level", (req, res) => __awaiter(void 0, void 0, void 0, function* () {
    try {
        const results = yield mod.find({ level: req.body.level }).sort({ score: -1, time: 1 }).limit(5).exec();
        res.send(results);
    }
    catch (error) {
        res.status(500).send(error);
    }
}));
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
