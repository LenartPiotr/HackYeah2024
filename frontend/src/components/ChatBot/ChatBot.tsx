import "./ChatBox.scss";
import { useEffect, useRef, useState } from "react";
import { MessageType, SummaryType } from '../../types';
import loadingGif from "../../assets/loading.gif";
import { useMutation } from "react-query";
import axios from "axios";
import { IoSendSharp } from "react-icons/io5";
import SpeechToText from "../SpeechToText/SpeechToText";

const ChatBot = ({ addResponses }: ChatBotProps) => {
  const [message, setMessage] = useState<string>("");
  const [chatData, setChatData] = useState<MessageType[]>([{
    text: "Witaj, opisz mi swoją sytuację, abym mógł ci pomóc"
  }]);
  const [isLoading, setIsLoading] = useState<boolean>(false);
  const messageBox = useRef<HTMLDivElement>(null);
  const input = useRef<HTMLInputElement>(null);

  const postMessage = async (data: { response: string }) => {
    const response = await axios.post(`http://127.0.0.1:8000/message?response=${data.response}`);
    return response.data;
  };

  const mutation = useMutation(postMessage, {
    onMutate: () => {
      setChatData(chatData => [...chatData, {text: message, fromUser: true}]);
      setIsLoading(true);
    },
    onSuccess: (data) => {
      setChatData(chatData => [...chatData, { text: data.next_question }]);
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
            <span className="message">
              {message.text}
            </span>
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