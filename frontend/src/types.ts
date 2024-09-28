import { Languages } from "./enums";

type SummaryType = {
    category: string,
    type: string,
    response: string,
};

type Settings = {
    language: Languages
};

export type {
    SummaryType,
    Settings
};