type SummaryType = {
    category: string,
    type: string,
    response: string,
};

type MessageType = {
    text: string,
    fromUser?: boolean;
}

export type {
    SummaryType,
    MessageType
};