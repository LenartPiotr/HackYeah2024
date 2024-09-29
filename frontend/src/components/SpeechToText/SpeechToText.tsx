import { useState } from 'react';
import './speechToText.scss';
import { FaMicrophone } from "react-icons/fa6";
import classNames from 'classnames';

const SpeechToText = ({ setMessage }: SpeechToTextProps) => {

    const [isActive, setIsActive] = useState(false);

    const recordSpeech = () => {
        const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
        const recognition = new SpeechRecognition();

        recognition.onresult = async function(event) {
            const transcript = event.results[0][0].transcript;
            setMessage(transcript);
        }

        if(!isActive) {
            recognition.start();
            setIsActive(true);
        } else {
            recognition.stop();
            setIsActive(false);
        }
    };

    return (
        <button 
            type="button" 
            className={classNames('mic', {
                'active': isActive === true,
            })}
            onClick={recordSpeech}
        >
            <FaMicrophone size="20px" />
        </button>
    );
};

type SpeechToTextProps = {
    setMessage: (value: string) => void,
}

export default SpeechToText;