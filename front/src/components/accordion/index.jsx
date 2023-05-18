import "./styles.css"
import * as Accordion from '@radix-ui/react-accordion';
import { ChevronDownIcon } from '@radix-ui/react-icons';
import React from "react";

const AccordionDemo = ({ graphs }) => (
    <Accordion.Root className="AccordionRoot" type="single" defaultValue="item-1" collapsible>
        {
            graphs && graphs.length > 0 && graphs.map((item, index) => {
                return (
                    <Accordion.Item className="AccordionItem" value={"item-" + index}>
                        <AccordionTrigger>{item.name}</AccordionTrigger>
                        <AccordionContent>
                            <img src={"data:image/jpeg;base64, " + item.graph} style={{ backgroundColor: "red", width: '200px', height: 'auto' }} />
                        </AccordionContent>
                    </Accordion.Item>
                )
            })
        }
    </Accordion.Root>
);

const AccordionTrigger = React.forwardRef(({ children, className, ...props }, forwardedRef) => (
    <Accordion.Header className="AccordionHeader">
        <Accordion.Trigger
            className={'AccordionTrigger'}
            {...props}
            ref={forwardedRef}
        >
            {children}
            <ChevronDownIcon className="AccordionChevron" aria-hidden />
        </Accordion.Trigger>
    </Accordion.Header>
));

const AccordionContent = React.forwardRef(({ children, className, ...props }, forwardedRef) => (
    <Accordion.Content
        className={'AccordionContent'}
        {...props}
        ref={forwardedRef}
    >
        <div className="AccordionContentText">{children}</div>
    </Accordion.Content>
));

export default AccordionDemo;