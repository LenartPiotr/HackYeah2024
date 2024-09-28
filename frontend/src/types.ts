import { Languages } from "./enums";

type SummaryType = {
    category: string,
    type: string,
    response: string,
};

type MessageType = {
    text: string,
    fromUser?: boolean;
}

type Settings = {
    language: Languages
};

export type {
    SummaryType,
    MessageType,
    Settings
};