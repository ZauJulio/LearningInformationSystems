import styles from "../styles/components/Pagination.module.scss";

interface PaginationProps {
  total: number;
  current: number;
  handler: Function;
}

const PageNumber = ({ index, handler }) => {
  return (
    <button
      className={styles.buttonActive}
      type="button"
      onClick={() => {
        handler(index);
      }}
    >
      <u>{index}</u>
    </button>
  );
};

export default function Pagination(props: PaginationProps) {
  var pages = [];
  console.log(props.total);
  for (var i = 1; i <= props.total; i++) {
    if (i === props.current) {
      pages.push(<p key={i}>{i}</p>);
    } else {
      pages.push(<PageNumber key={i} index={i} handler={props.handler} />);
    }
  }
  return <div className={styles.paginationContainer}>{pages}</div>;
}
