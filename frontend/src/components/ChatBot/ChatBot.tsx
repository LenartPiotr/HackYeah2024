import "./ChatBox.scss";
import { useEffect, useRef, useState } from "react";
import { MessageType, SummaryType } from '../../types';
import loadingGif from "../../assets/loading.gif";
import { useMutation } from "react-query";
import axios from "axios";
import { IoSendSharp } from "react-icons/io5";
import SpeechToText from "../SpeechToText/SpeechToText";

const formNames: string[] = ["PCC-2", "PCC-3", "PCC-3/A", "PCC-4", "PCC-4/A", "SD-2", "SD-3", "SD-3/A", "SD-Z2"];

const ChatBot = ({ addResponses }: ChatBotProps) => {
  const [message, setMessage] = useState<string>("");
  const [chatData, setChatData] = useState<MessageType[]>([{
    text: "Witaj, opisz mi swoją sytuację, abym mógł ci pomóc"
  }]);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const messageBox = useRef<HTMLDivElement>(null);
  const input = useRef<HTMLInputElement>(null);

  useEffect(() => {
    window.addEventListener('eFormName', handleFormEvent);
  }, []);

  const handleFormEvent = (event: any) => {
    documentMutation.mutate({ response: event.detail.msg });
  }

  const postDocument = async (data: { response: string }) => {
    const response = await axios.post(`http://127.0.0.1:8000/select_document?document=${data.response}`);
    return response.data;
  }

  const postMessage = async (data: { response: string }) => {
    const response = await axios.post(`http://127.0.0.1:8000/message?response=${data.response}`);
    return response.data;
  };

  const parseMessage = (message: string) => {
    for(const formName of formNames) {
      const index = message.indexOf(formName);
      if(index >= 0) {
        const insert = `<a onclick="window.dispatchEvent(new CustomEvent('eFormName', {
          detail: { msg: '${formName}' }
        }))" href="#">${formName}</a>`;
        message = message.slice(0, index) + insert + message.slice(index + formName.length);
      }
    }
    return message;
  }

  const documentMutation = useMutation(postDocument, {
    onMutate: () => {
      setIsLoading(true);
    },
    onSuccess: (data) => {
      setChatData(chatData => [...chatData, { text: parseMessage(data.next_question) }]);
      addResponses(data.responses);
      setIsLoading(false);
    },
    onError: (error) => {
      console.error("Error sending message:", error);
      setIsLoading(false);
    },
  });

  const mutation = useMutation(postMessage, {
    onMutate: () => {
      setChatData(chatData => [...chatData, {text: message, fromUser: true}]);
      setIsLoading(true);
    },
    onSuccess: (data) => {
      setChatData(chatData => [...chatData, { text: parseMessage(data.next_question) }]);
      addResponses(data.responses);
      setIsLoading(false);
    },
    onError: (error) => {
      console.error("Error sending message:", error);
      setIsLoading(false);
    },
  });

  useEffect(() => {
    if(messageBox.current) {
      messageBox.current.scrollTop = messageBox.current.scrollHeight;
    }
  }, [chatData])

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    
    if(!message) {
      return;
    }

    mutation.mutate({ response: message });
    
    setMessage("");
  }

  const handleButton = () => {
    input.current?.focus();
  }

  return (
    <form onSubmit={handleSubmit} className="chat-box">
      <div className="messages" ref={messageBox}>
        {chatData.map((message, index) => <>
          <div key={index} className={`message-wrapper ${message.fromUser ? "from-user" : ""}`}>
            {!message.fromUser && <div className="avatar"></div>}
            <span className="message" dangerouslySetInnerHTML={{__html: message.text}} />
          </div>
        </>)}
        {isLoading && <img width="32" height="32" src={loadingGif} />}
      </div>
      <div className="input-row">
        <div className="input-wrapper">
          <input name="message" ref={input} value={message} onChange={(e) => setMessage(e.target.value)} autoComplete="off"/>
          <button className="send" onClick={handleButton}>
            <IoSendSharp />
          </button>
        </div>
        <SpeechToText setMessage={setMessage} />
      </div>
    </form>
  )
};

type ChatBotProps = {
  addResponses: (responseData: SummaryType[]) => void,
};

export default ChatBot;